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
    async def youtube(self, ctx, *, search):
        number = 1
        if "," in search:
            full = search.split(",")
            search = full[0].replace(' ', '+')
            number = int(full[1])
        links = await LinkGrabber.videograbber(search, min(10, number))
        for link in links:
            await ctx.send(link)
        await self.MongoWorker.add_youtube("yt", search, ctx.message.author, ctx.message.guild)



async def setup(client):
    await client.add_cog(Youtube(client))

