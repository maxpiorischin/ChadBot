import discord
from discord.ext import commands
from ..modules import ytVideoGrabber
from replit import db


class Youtube(commands.Cog):
    """Youtube Commands"""

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command(aliases = ["yt"])
    async def youtube(self, ctx, message):
        if type(message) == str:
            link = ytVideoGrabber.videograbber(message)
            await ctx.send(link)
        else:
            await ctx.send("error")



def setup(client):
    client.add_cog(Youtube(client))

