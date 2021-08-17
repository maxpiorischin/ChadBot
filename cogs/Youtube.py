import discord
from discord.ext import commands
import sys
sys.path.append("..")
from modules import LinkGrabber, Mongo


class Youtube(commands.Cog):
    """Youtube Commands"""

    def __init__(self, client):
        self.client = client
        self.MongoWorker = Mongo.MongoWorker()

    # commands

    @commands.command(aliases = ["yt"])
    async def youtube(self, ctx, *search):
        search_term = '+'.join(search)
        print("searching: " +search_term)
        link = LinkGrabber.videograbber(search_term)
        await ctx.send(link)
        await self.MongoWorker.add_youtube("yt", search_term, ctx.message.author, ctx.message.guild)



def setup(client):
    client.add_cog(Youtube(client))

