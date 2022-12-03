import discord
from discord.ext import commands
import random
import pymongo
from pymongo import MongoClient
import os, sys
sys.path.append("..")
from modules import Mongo, tools

class Settings(commands.Cog):
    """ Bot Settings, including prefix changing"""
    def __init__(self, client):
        self.client = client
        self.MongoWorker = Mongo.MongoWorker()

    # gets the prefix from database
    async def get_prefix(self, client, message):
        prefix = await self.MongoWorker.get_prefix(message)
        return prefix

    #events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        await self.MongoWorker.add_prefix(guild.id, ".")

        general = guild.text_channels[0]
        if general and general.permissions_for(guild.me).send_messages:
            await general.send(f"``` Hello {guild.name} ! \n I am Chad and you could use .help for a list of my commands! ```")

        print(f"Joined Guild {guild.name} - {guild.id}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        await self.MongoWorker.del_prefix(guild.id)

    #commands

    @commands.command()
    @commands.has_permissions()
    async def changeprefix(self, ctx, prefix = '.'):
        if ctx.message.author.guild_permissions.administrator:
            await self.MongoWorker.update_prefix(ctx.message.guild.id, prefix)

            message = f"Prefix changed to {prefix}"
            embed = tools.embed_creator("Settings", message, discord.Color.green())
            await ctx.send("", embed = embed)
        else:
            embed = tools.embed_creator("ERROR", "Only Admins can use this command!", discord.Color.green())
            await ctx.send("", embed = embed)
    


async def setup(client):
    await client.add_cog(Settings(client))
