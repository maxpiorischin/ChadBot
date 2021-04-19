import discord
from discord.ext import commands
import random

class About(commands.Cog):
    """ Gives info about the bot information"""
    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def info(self, ctx):
        await ctx.send("``` I'm a bot created by xxsuka#7765\n Server count: {} ```".format(len(self.client.guilds)))
    
        


def setup(client):
    client.add_cog(About(client))