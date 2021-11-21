import discord
from discord.ext import commands
import sys
from selenium import webdriver
import os, time
sys.path.append("..")
from modules import Mongo, tools

option = webdriver.ChromeOptions()

option.binary_location = os.getenv('GOOGLE_CHROME_BIN')
option.add_argument("--headless")
option.add_argument('--disable-gpu')
option.add_argument('--no-sandbox')

sys.path.append("..")
from modules import LinkGrabber

class Google(commands.Cog):
    """Google Commands"""

    def __init__(self, client):
        self.client = client
        self.driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=option)
        self.MongoWorker = Mongo.MongoWorker()

    # commands
    # THE COMMENTS REPRESENT THE OLD CODE, WITH LIMITED API IMAGE LOADING
    @commands.command(aliases=["pic", "image"])
    async def img(self, ctx, *search_comma_numberlessthan11):
        tic = time.perf_counter()
        try:
            if search_comma_numberlessthan11 == None:
                ctx.send("Please add an input!")
                return
            message = await ctx.send("loading image...")
            search_term = '+'.join(search_comma_numberlessthan11)
            last_val = search_term[len(search_term.rstrip('0123456789')):]
            if last_val.isdigit():
                if int(last_val) > 10 and "," in search_term:
                    embed = tools.embed_creator("ERROR", "Maximum of 10 Images!", discord.Color.red())
                    await ctx.send("", embed = embed)
                    return
                if (search_term.endswith(",+" + last_val)) and 0 < int(last_val) <= 10:
                    search_term = search_term[:-(len(last_val) + 2)]
                    print("searching: " + search_term + " " + last_val, "in ", ctx.guild.name)
                    link = await LinkGrabber.imagegrabber(search_term, self.driver, int(last_val) - 1)
                    #link = LinkGrabber.googleapiimagegrabber(search_term, int(last_val))
                    print(search_term, int(last_val), link)
                    for i in link:
                        await ctx.send(i)
                    await self.MongoWorker.add_img(search_term, ctx.message.author, ctx.message.guild)
                    return

            link = await LinkGrabber.imagegrabber(search_term, self.driver, 1)
            print(search_term, link)
            link = link[0]
            #link = LinkGrabber.googleapiimagegrabber(search_term, 1)[0]
            print("searching: " + search_term)
            await message.edit(content=link)
            await self.MongoWorker.add_img(search_term, ctx.message.author, ctx.message.guild)
        except:
            embed = tools.embed_creator("No Result!", "", discord.Color.blue())
            await ctx.send("", embed = embed)
            search_term = '+'.join(search_comma_numberlessthan11)
            await self.MongoWorker.add_img(search_term, ctx.message.author, ctx.message.guild)
        toc = time.perf_counter
        print(f"Time to search image: {toc-tic}")

    @commands.command(aliases=["smallpic", "spic", "simg", "smallimage"])
    async def smallimg(self, ctx, *search):
        try:
            search_term = '+'.join(search)
            print("searching: " + search_term, "in ", ctx.guild.name)
            link = await LinkGrabber.smallimagegrabber(search_term)
            await ctx.send(link)
            await self.MongoWorker.add_img(search_term, ctx.message.author, ctx.message.guild)
        except:
            embed = tools.embed_creator("No Result!", "", discord.Color.blue())
            await ctx.send("", embed = embed)
            search_term = '+'.join(search)
            await self.MongoWorker.add_img(search_term, ctx.message.author, ctx.message.guild)

    @commands.command(aliases=["google", "find"])
    async def search(self, ctx, *search):
        try:
            search_term = ' '.join(search)
            link = await LinkGrabber.googlesearch(search_term)
            await ctx.send(link)
            await self.MongoWorker.add_web("search", search_term, ctx.message.author, ctx.message.guild)
        except:
            await ctx.send("No Result!")
            search_term = ' '.join(search)
            await self.MongoWorker.add_web("search", search_term, ctx.message.author, ctx.message.guild)

    @commands.command()
    async def define(self, ctx, *search):
        try:
            search_term = '%20'.join(search)
            embed_search = ' '.join(search)
            print("searching definition for: ", search_term, "in ", ctx.guild.name)
            defin = await LinkGrabber.defingrabber(search_term)
            """ discord embed version
            embed = discord.Embed(
                title=embed_search + " Definition:",
                description=defin,
                color=discord.Color.blue()
            )
            await ctx.send("", embed = embed)
            """
            await ctx.send(defin)
            await self.MongoWorker.add_web("define", search_term, ctx.message.author, ctx.message.guild)
        except:
            await ctx.send("No Result!")
            search_term = '%20'.join(search)
            await self.MongoWorker.add_web("define", search_term, ctx.message.author, ctx.message.guild)



def setup(client):
    client.add_cog(Google(client))
