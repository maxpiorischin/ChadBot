import discord
from discord.ext import commands
from discord.utils import find
import json
import os
import random

gifs_list = ["vibecat", "ridecat", "trumpetcat", "rainbowroach"]
token = os.getenv("CHAD_BOT_TOKEN")


# gets the prefix from the json file
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


if __name__ == '__main__':
    client = commands.Bot(command_prefix=get_prefix)


    @client.event
    async def on_ready():
        members = 0
        for guild in client.guilds:
            members += guild.member_count
        await client.change_presence(status=discord.Status.online,
                                     activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=f"{members} users!"))
        print("Chad is ready!")


    @client.event
    async def on_guild_join(guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(guild.id)] = "."

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        general = guild.text_channels[0]
        if general and general.permissions_for(guild.me).send_messages:
            await general.send(f"``` Hello {guild.name} ! \n I am Chad and you could use .help for a list of my commands! ```")

    @client.event
    async def on_guild_remove(guild):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)


    @client.command()
    @commands.has_permissions(administrator=True)
    async def changeprefix(ctx, prefix):
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f"Prefix changed to {prefix}")


    @client.command()
    async def info(ctx):
        await ctx.send("``` I'm a bot created by xxsuka#7765\n Server count: {} ```".format(len(client.guilds)))


    @client.command()
    async def hello(ctx):
        await ctx.send("Hello, I am Chad")


    @client.command()
    async def sheesh(ctx):
        x = "e" * random.randrange(2, 30)
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
        await ctx.send("```Gif commands are: " + message + " ```")


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
