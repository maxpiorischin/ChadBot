import discord
from discord.ext import commands
import random

class Servermanagement(commands.Cog):
    """Managing Server (Requires admin permissions)"""
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount = 5):
      try:
        await ctx.channel.purge(limit = amount + 1)
      except:
        await ctx.send("Bot or user Manage Message permission not granted!")


def setup(client):
    client.add_cog(Servermanagement(client))