import discord
from discord.ext import commands
import sys
from selenium import webdriver
import os

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

    # commands
    # THE COMMENTS REPRESENT THE OLD CODE, WITH SELENIUM IMAGE LOADING
    @commands.command(aliases=["pic", "imagesearch"])
    async def img(self, ctx, *search_comma_numberlessthan11):
        if search_comma_numberlessthan11 == None:
            ctx.send("Please add an input!")
            return
        message = await ctx.send("loading image...")
        # driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=option)
        search_term = '+'.join(search_comma_numberlessthan11)
        last_val = search_term[len(search_term.rstrip('0123456789')):]
        if last_val.isdigit():
            if (search_term.endswith(",+" + last_val)) and 0 < int(last_val) <= 10:
                search_term = search_term[:-(len(last_val) + 2)]
                print("searching: " + search_term + " " + last_val)
                # link = LinkGrabber.imagegrabber(search_term, driver, int(last_val))
                link = LinkGrabber.apiimagegrabber(search_term, int(last_val))
                print(search_term, int(last_val), link)
                for i in link:
                    await ctx.send(i)
                return

        # link = LinkGrabber.imagegrabber(search_term, driver, 1)[0]
        link = LinkGrabber.apiimagegrabber(search_term, 1)[0]
        print("searching: " + search_term)
        await message.edit(content=link)
        # driver.quit()

    @commands.command(aliases=["smallpic", "spic", "simg", "smallimage"])
    async def smallimg(self, ctx, *search):
        search_term = '+'.join(search)
        print("searching: " + search_term)
        link = LinkGrabber.smallimagegrabber(search_term)
        await ctx.send(link)

    @commands.command(aliases=["google", "find"])
    async def search(self, ctx, *search):
        search_term = ' '.join(search)
        link = LinkGrabber.googlesearch(search_term)
        await ctx.send(link)


def setup(client):
    client.add_cog(Google(client))
