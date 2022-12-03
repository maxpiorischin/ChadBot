import discord
from discord.ext import commands
#test
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
            await ctx.send("https://cdn.discordapp.com/attachments/491423048751382548/834229712682745886/latest.png")
        else:
            print("someone else trying to use fortnut")

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def washed(self, ctx):
        if ctx.message.guild.id == self.server_id:
            await ctx.send("https://cdn.discordapp.com/attachments/453664765605314561/835365199900966972/beef-patty-side_Cut-Out.png")
        else:
            print("someone else trying to use fortnut")\

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def suka(self, ctx):
        if ctx.message.guild.id == self.server_id:
            await ctx.send("https://cdn.discordapp.com/attachments/833549338373521441/835366167081517066/MS5CAkN.png")
        else:
            print("someone else trying to use fortnut")

    @commands.command()
    async def hardpurge(self, ctx, amount=5):
        try:
            if ctx.message.author.id == 281621038771732481:
                await ctx.channel.purge(limit=amount + 1)
            else:
                await ctx.send("Only Bot owner can use this command :)")
        except:
            await ctx.send("Bot permission not granted!")

    



async def setup(client):
    await client.add_cog(Fortnut(client))
