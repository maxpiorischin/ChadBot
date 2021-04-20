import discord
from discord.ext import commands


class Fortnut(commands.Cog):
    """ Gives info about the bot information"""

    def __init__(self, client):
        self.client = client
        self.server_id = 453664765181427723

    # commands
    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def pep(self, ctx):
        if ctx.message.guild.id == self.server_id:
            await ctx.send("https://cdn.discordapp.com/emojis/833859474062049320.png?v=1")
        else:
            print("someone else trying to use fortnut")





def setup(client):
    client.add_cog(Fortnut(client))