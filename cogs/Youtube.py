import discord
from discord.ext import commands
from replit import db


class Youtube(commands.Cog):
    """Bot Information"""

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def youtube(self, ctx):
        await ctx.send("Youtube Command, work in progress")



def setup(client):
    client.add_cog(Youtube(client))