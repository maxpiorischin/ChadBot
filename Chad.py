import discord, os, asyncio
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv

from modules.tools import quick_embed
from modules.ahttp import HTTP

load_dotenv()

token = os.getenv("CHAD_BOT_TOKEN")
cluster = MongoClient(os.getenv("MONGODB_CONNECTION"))
google_search = os.getenv("GOOGLE_SEARCH")

db = cluster["Chad"]
prefixes = db["Prefixes"]
# Change only the no_category default string
help_command = commands.DefaultHelpCommand(no_category="ModifyExtensions")

# invite https://discord.com/api/oauth2/authorize?client_id=833176607496863804&permissions=8&scope=bot
# non admin https://discord.com/api/oauth2/authorize?client_id=833176607496863804&permissions=67234880&scope=bot
# Developed By Maxim Piorischin, github.com/maxpiorischin

# gets the prefix from database
def get_prefix(client, message):
    prefix = "."
    if message.guild is not None:
        post = prefixes.find_one({"_id": str(message.guild.id)})
        prefix = post["prefix"]
    return prefix


if __name__ == "__main__":

    # adds quick embed to the base context
    async def embed_wrapper(self_i, **kwargs):
        return await quick_embed(self_i, **kwargs)

    commands.Context.embed = embed_wrapper

    client = commands.Bot(command_prefix=get_prefix, help_command=help_command, intents=discord.Intents.all())
    client.remove_command("help")
    client.ahttp = HTTP()

    @client.event
    async def on_ready():
        members = 0
        for guild in client.guilds:
            members += guild.member_count
        await client.change_presence(
            status=discord.Status.online,
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=f"{members} users!"
            ),
        )
        print("Chad is ready!")

    @client.command()
    async def load(ctx, extension):
        await client.load_extension(f"cogs.{extension}")

    @client.command()
    async def unload(ctx, extension):
        await client.unload_extension(f"cogs.{extension}")

    async def load_extensions():  
        print("-------------------")
        for cog in os.listdir("./cogs"):
            if cog.endswith(".py"):
                try:
                    await client.load_extension(f"cogs.{cog[:-3]}")
                    print(f"{cog} Loaded!")
                except Exception as e:
                    print(f"{cog} cannot be loaded:")
                    raise e
    print("-------------------")

    async def main():
        async with client:
            await load_extensions()
            await client.start(token)

    asyncio.run(main())

