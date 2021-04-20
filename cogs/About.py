import discord
from discord.ext import commands

class About(commands.Cog):
    """ Gives info about the bot information"""
    def __init__(self, client):
        self.client = client

    #commands
    @commands.command()
    async def info(self, ctx):
        await ctx.send("``` I'm a bot created by xxsuka#7765\n Server count: {} ```".format(len(self.client.guilds)))

    @commands.command()
    @commands.has_permissions(embed_links = True)
    async def help(self, ctx):
        embed = discord.Embed(title="How to use ChadBot")
        for cog in self.client.cogs:
            embed.add_field(name = cog.name, value = '')
            for command in cog.get_commands:
                embed.add_field(name= command.name, value = '')
        await ctx.send(content = None, embed = embed)


        


def setup(client):
    client.add_cog(About(client))