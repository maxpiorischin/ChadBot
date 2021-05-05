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

    @commands.command(aliases=["pic", "imagesearch"])
    async def img(self, ctx, *search):
        message = await ctx.send("loading image...")
        driver = webdriver.Chrome(executable_path=os.getenv('CHROME_EXECUTABLE_PATH'), options=option)
        search_term = '+'.join(search)
        print("searching: " + search_term)
        link = LinkGrabber.imagegrabber(search_term, driver)
        await message.edit(content = link)
        driver.quit()

    @commands.command(aliases=["google", "find"])
    async def search(self, ctx, *search):
        search_term = ' '.join(search)
        link = LinkGrabber.googlesearch(search_term)
        await ctx.send(link)


def setup(client):
    client.add_cog(Google(client))
