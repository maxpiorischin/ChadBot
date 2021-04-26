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
        await ctx.channel.purge(limit = amount)


def setup(client):
    client.add_cog(Servermanagement(client))