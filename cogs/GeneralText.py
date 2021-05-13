import discord
from discord.ext import commands
import random, sys
sys.path.append("..")
from modules import Games

class General(commands.Cog):
    """General commands that respond with a message"""
    def __init__(self, client):
        self.client = client

    #commands
    @commands.command(aliases = ['hi'])
    async def hello(self, ctx):
        await ctx.send("Hello, I am Chad")

    @commands.command()
    async def sheesh(self, ctx):
        x = "e" * random.randrange(2, 30)
        await ctx.send("sh" + x + "sh")

    @commands.command()
    async def pp(self, ctx):
        message_author = ctx.message.author.name
        x = "=" * random.randrange(2, 40)
        await ctx.send(message_author + "'s pp length:  8" + x + "D")

    @commands.command()
    @commands.has_permissions(embed_links=True) #funny gif
    async def fart(self, ctx):
        await ctx.send("https://tenor.com/view/among-us-fart-poop-shit-fart-gif-18914562")

    @commands.command(aliases = ['8ball', 'question'])
    @commands.has_permissions(embed_links=True)  # funny gif
    async def _8ball(self, ctx, *search):
        msg = ' '.join(search)
        response = Games.response(msg)
        await ctx.send(response)
        print(response)




def setup(client):
    client.add_cog(General(client))

