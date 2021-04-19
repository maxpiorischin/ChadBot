import discord
from discord.ext import commands
import random

class Gifs(commands.Cog):
    """ Gifs commands """
    def __init__(self, client):
        self.client = client
        self.gifs_list = ["vibecat", "ridecat", "trumpetcat", "rainbowroach"]

    #commands
    @commands.command()
    async def gifs(self, ctx):
        message = ""
        for gif in self.gifs_list:
            message += gif + "  "
        await ctx.send("```Gif commands are: " + message + " ```")


    @commands.command()
    async def vibecat(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/817502837453619231.gif?v=1")


    @commands.command()
    async def ridecat(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833214796534251521.gif?v=1")


    @commands.command()
    async def trumpetcat(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833209656947113984.gif?v=1")


    @commands.command()
    async def rainbowroach(self, ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833211453346807858.gif?v=1")


def setup(client):
    client.add_cog(Gifs(client))