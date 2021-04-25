import discord
from discord.ext import commands
import sys
sys.path.append("..")
from modules import ytVideoGrabber


class Musicplayer(commands.Cog):
    """Playing Music in a voice channel"""

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def play(self, ctx, *search):
        search_term = '+'.join(search)
        link = ytVideoGrabber.videograbber(search_term)
        print("playing " + search_term)
        await ctx.send(link)



def setup(client):
    client.add_cog(Musicplayer(client))