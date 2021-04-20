import discord
from discord.ext import commands
import random
from replit import db

class Settings(commands.Cog):
    """ Bot Settings, including prefix changing"""
    def __init__(self, client):
        self.client = client

    # gets the prefix from database
    def get_prefix(self, client, message):
      return db[str(message.guild.id)]

    #events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        db[str(guild.id)] = "."

        general = guild.text_channels[0]
        if general and general.permissions_for(guild.me).send_messages:
            await general.send(f"``` Hello {guild.name} ! \n I am Chad and you could use .help for a list of my commands! ```")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        del db[str(guild.id)]

    #commands

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):

        db[str(ctx.guild.id)] = prefix

        message = f"Prefix changed to {prefix}"
        print(message)
        await ctx.send(message)
    


def setup(client):
    client.add_cog(Settings(client))