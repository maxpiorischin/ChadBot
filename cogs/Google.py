import discord
from discord.ext import commands
import sys
sys.path.append("..")
from modules import LinkGrabber


class Google(commands.Cog):
    """Google Commands"""

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command(aliases = ["pic", "imagesearch"])
    async def img(self, ctx, *search):
        search_term = '+'.join(search)
        print("searching: " +search_term)
        link = LinkGrabber.imagegrabber(search_term)
        await ctx.send(link)



def setup(client):
    client.add_cog(Google(client))