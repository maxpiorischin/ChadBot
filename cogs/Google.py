import discord
from discord.ext import commands
import sys
from selenium import webdriver
import os
from time import perf_counter
import aiohttp
import datetime

sys.path.append("..")
from modules import Mongo, tools
from urllib.parse import quote

from Chad import google_search


option = webdriver.ChromeOptions()

option.binary_location = os.getenv("GOOGLE_CHROME_BIN")
option.add_argument("--headless")
option.add_argument("--disable-gpu")
option.add_argument("--no-sandbox")

sys.path.append("..")
from modules import LinkGrabber
from smalldata import BanList


get_fukt = "https://mime.rcp.r9n.co/memes/default?image=https://cdn.discordapp.com/attachments/829072008733261834/918301693186297856/unknown.png"
invis = 0x2F3136


class Google(commands.Cog):
    """Google Commands"""

    def __init__(self, client):
        self.client = client
        self.driver = webdriver.Chrome(
            executable_path=os.getenv("CHROME_EXECUTABLE_PATH"), options=option
        )
        self.MongoWorker = Mongo.MongoWorker()
        self.banlist = BanList.banlist
        self.link_cache = {}

    # commands
    # THE COMMENTS REPRESENT THE OLD CODE, WITH LIMITED API IMAGE LOADING

    @commands.command(aliases=["pic", "image"])
    async def img(
        self, ctx: commands.Context, *, content: commands.clean_content = None
    ):
        tic = perf_counter()
        if ctx.message.author in self.banlist:
            msg = f"{get_fukt}&top=get_fukt_{quote(ctx.message.author.name)}&bottom=ur_banned"
            return await ctx.embed(image_url=msg, color=invis)

        if content is None:
            return await ctx.embed(title="Missing Search Term", color=invis)

        number = 1
        if "," in content:
            stuff = content.split(",")
            content = ",".join(stuff[:-1])
            number = max(
                min(int(stuff[-1].strip()) if stuff[-1].strip().isdigit() else 1, 10), 1
            )

        search_term = quote(content)

        print(f"searching: {content} | {number} \t in {ctx.guild.name}")

        links = self.link_cache.get(content, [])
        # if content in self.link_cache:
        #     c_links, timestamp = self.link_cache[content]
        #     if len(c_links) == 0:
        #         del self.link_cache[content]
        #     else:
        #         if (datetime.datetime.now().timestamp() - timestamp) < 3600:
        #             links = c_links
        #         else:
        #             del self.link_cache[content]

        if len(links) == 0:
            j_links = await self.client.ahttp.get_json(google_search + search_term)
            if j_links != {} and len(j_links) > 0:
                links = j_links
                self.link_cache[content] = links
            # self.link_cache[content] = [
            #     links,
            #     datetime.datetime.now().timestamp(),
            # ]

        await self.MongoWorker.add_img(content, ctx.message.author, ctx.message.guild)

        if len(links) == 0:
            return await ctx.embed(title="No Results Found!", color=invis)

        i = 0
        sent = False
        for link in links:
            if i == number:
                break

            # if await self.client.ahttp.is_media(link): THIS IS FOR MORE STRICT
            i += 1
            sent = True
            await ctx.reply(content=link, mention_author=False)

        if not sent:
            return await ctx.embed(title="No Results Found!", color=invis)

            # await ctx.embed(
            #     image_url=link, footer={"text": f"search term: {content}"}, color=invis
            # )'
        toc = perf_counter()
        time = toc - tic
        #await ctx.send(f"Time to search image with gurgle: {time}")
        print(f"Time to search image with gurgle: {time}")

    @commands.command(aliases=["oimg", "im"])
    async def ogimg(self, ctx: commands.Context, *search_comma_numberlessthan11):
        tic = perf_counter()
        if ctx.message.author in self.banlist:
            msg = f"https://mime.rcp.r9n.co/memes/default?image=https://cdn.discordapp.com/attachments/829072008733261834/918301693186297856/unknown.png&top=get_fukt_{quote(ctx.message.author.name)}&bottom=ur_banned"
            await ctx.send(msg)
            # embed = discord.Embed(
            #     title="Error!",
            #     description="You're banned",
            #     color=discord.Color.red()
            # )
            # await ctx.send("", embed=embed)
            return
        try:
            if search_comma_numberlessthan11 == None:
                ctx.send("Please add an input!")
                return
            message = await ctx.send("loading image...")
            search_term = "+".join(search_comma_numberlessthan11)
            last_val = search_term[len(search_term.rstrip("0123456789")) :]
            if last_val.isdigit():
                if int(last_val) > 10 and "," in search_term:
                    embed = tools.embed_creator(
                        "ERROR", "Maximum of 10 Images!", discord.Color.red()
                    )
                    await ctx.send("", embed=embed)
                    return
                if (search_term.endswith(",+" + last_val)) and 0 < int(last_val) <= 10:
                    search_term = search_term[: -(len(last_val) + 2)]
                    print(
                        "searching: " + search_term + " " + last_val,
                        "in ",
                        ctx.guild.name,
                    )
                    link = await LinkGrabber.imagegrabber(
                        search_term, self.driver, int(last_val) - 1
                    )
                    # link = LinkGrabber.googleapiimagegrabber(search_term, int(last_val))
                    print(search_term, int(last_val), link)
                    for i in link:
                        await ctx.send(i)
                    await self.MongoWorker.add_img(
                        search_term, ctx.message.author, ctx.message.guild
                    )
                    return

            link = await LinkGrabber.imagegrabber(search_term, self.driver, 1)
            print(search_term, link)
            link = link[0]
            # link = LinkGrabber.googleapiimagegrabber(search_term, 1)[0]
            print("searching: " + search_term)
            await message.edit(content=link)
            await self.MongoWorker.add_img(
                search_term, ctx.message.author, ctx.message.guild
            )
        except:
            embed = tools.embed_creator("No Result!", "", discord.Color.blue())
            await ctx.send("", embed=embed)
            search_term = "+".join(search_comma_numberlessthan11)
            await self.MongoWorker.add_img(
                search_term, ctx.message.author, ctx.message.guild
            )
        toc = perf_counter()
        time = toc - tic
        #await ctx.send(f"Time to search image with selenium: {time}")
        print(f"Time to search image with selenium: {time}")

    @commands.command(aliases=["smallpic", "spic", "simg", "smallimage"])
    async def smallimg(self, ctx, *search):
        if ctx.message.author in self.banlist:
            msg = f"https://mime.rcp.r9n.co/memes/default?image=https://cdn.discordapp.com/attachments/829072008733261834/918301693186297856/unknown.png&top=get_fukt_{quote(ctx.message.author.name)}&bottom=ur_banned"
            await ctx.send(msg)
            # embed = discord.Embed(
            #     title="Error!",
            #     description="You're banned",
            #     color=discord.Color.red()
            # )
            # await ctx.send("", embed=embed)
            return
        try:
            search_term = "+".join(search)
            print("searching: " + search_term, "in ", ctx.guild.name)
            link = await LinkGrabber.smallimagegrabber(search_term)
            await ctx.send(link)
            await self.MongoWorker.add_img(
                search_term, ctx.message.author, ctx.message.guild
            )
        except:
            embed = tools.embed_creator("No Result!", "", discord.Color.blue())
            await ctx.send("", embed=embed)
            search_term = "+".join(search)
            await self.MongoWorker.add_img(
                search_term, ctx.message.author, ctx.message.guild
            )

    @commands.command(aliases=["google", "find"])
    async def search(self, ctx, *search):
        try:
            search_term = " ".join(search)
            link = await LinkGrabber.googlesearch(search_term)
            await ctx.send(link)
            await self.MongoWorker.add_web(
                "search", search_term, ctx.message.author, ctx.message.guild
            )
        except:
            await ctx.send("No Result!")
            search_term = " ".join(search)
            await self.MongoWorker.add_web(
                "search", search_term, ctx.message.author, ctx.message.guild
            )

    @commands.command()
    async def define(self, ctx, *search):
        try:
            search_term = "%20".join(search)
            embed_search = " ".join(search)
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
            await self.MongoWorker.add_web(
                "define", search_term, ctx.message.author, ctx.message.guild
            )
        except:
            await ctx.send("No Result!")
            search_term = "%20".join(search)
            await self.MongoWorker.add_web(
                "define", search_term, ctx.message.author, ctx.message.guild
            )


def setup(client):
    client.add_cog(Google(client))
