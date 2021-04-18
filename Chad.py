import discord
import Token
import os
from discord.ext import commands

gifs_list = ["vibecat", "ridecat", "trumpetcat", "rainbowroach"]

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
    async def gifs(ctx):
        message = ""
        for gif in gifs_list:
            message+= gif + "  "
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



    client.run(os.getenv('TOKEN'))

