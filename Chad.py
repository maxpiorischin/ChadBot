import discord
import os
import random
from discord.ext import commands

gifs_list = ["vibecat", "ridecat", "trumpetcat", "rainbowroach"]
token = os.getenv("CHAD_BOT_TOKEN")

if __name__ == '__main__':
    client = commands.Bot(command_prefix=".")


    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Hmmmmm"))
        print("Chad is ready!")


    @client.command()
    async def hello(ctx):
        await ctx.send("Hello, I am Chad")

    @client.command()
    async def sheesh(ctx):
        x = "e" * random.randrange(2,30)
        await ctx.send("sh" + x + "sh")

    @client.command()
    async def pp(ctx):
        message_author = ctx.message.author.name
        x = "=" * random.randrange(2, 40)
        await ctx.send(message_author + "'s pp length:  8" + x + "D")

    @client.command()
    async def gifs(ctx):
        message = ""
        for gif in gifs_list:
            message += gif + "  "
        await ctx.send("Gif commands are: " + message)


    @client.command()
    async def vibecat(ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/817502837453619231.gif?v=1")


    @client.command()
    async def ridecat(ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833214796534251521.gif?v=1")


    @client.command()
    async def trumpetcat(ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833209656947113984.gif?v=1")


    @client.command()
    async def rainbowroach(ctx):
        await ctx.send("https://cdn.discordapp.com/emojis/833211453346807858.gif?v=1")


    client.run(token)
