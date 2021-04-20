import discord
from discord.ext import commands
import random

class General(commands.Cog):
    """General commands that respond with a message"""
    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I am Chad")

    @commands.command()
    async def sheesh(self, ctx):
        x = "e" * random.randrange(2, 30)
        await ctx.send("sh" + x + "sh")

    @commands.command()
    async def pp(self, ctx):
        message_author = ctx.message.author.name
        x = "=" * random.randrange(2, 40)
        await ctx.send(message_author + "'s pp length:  8" + x + "D")


def setup(client):
    client.add_cog(General(client))

