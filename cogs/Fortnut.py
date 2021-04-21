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

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def logi(self, ctx):
      if ctx.message.guild.id == self.server_id:
        await ctx.send("https://media.tenor.com/images/1fc51a108537b70975aa749bab7f3935/tenor.gif")
      else:
        print("someone else trying to use fortnut")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def mark(self, ctx):
      if ctx.message.guild.id == self.server_id:
        await ctx.send("https://thumbs.gfycat.com/EverySevereAtlanticridleyturtle-size_restricted.gif")
      else:
        print("someone else trying to use fortnut")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def kiwi(self, ctx):
        if ctx.message.guild.id == self.server_id:
            await ctx.send("https://pngimg.com/uploads/kiwi/kiwi_PNG4030.pngWW")
        else:
            print("someone else trying to use fortnut")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def washed(self, ctx):
        if ctx.message.guild.id == self.server_id:
            await ctx.send("https://cdn.discordapp.com/attachments/491423048751382548/834229981117677579/wp2523652.png")
        else:
            print("someone else trying to use fortnut")





def setup(client):
    client.add_cog(Fortnut(client))