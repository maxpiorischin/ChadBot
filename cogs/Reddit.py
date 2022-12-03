import discord
from discord.ext import commands
import sys
import os

sys.path.append("..")
from modules import LinkGrabber

class Reddit(commands.Cog):
    """Reddit Commands"""

    def __init__(self, client):
        self.client = client


    # commands




async def setup(client):
    await client.add_cog(Reddit(client))
