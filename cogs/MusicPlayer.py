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
        voiceChannel = ctx.message.author.voice.voice_channel
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        if not voice.is_connected():
            await voiceChannel.connect()

        print("playing " + search_term)
        await ctx.send(link)

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("I'm not In a Voice Channel!")

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Currently nothing is playing")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Audio already playing")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_client, guild=ctx.guild)
        if voice.is_playing():
            await voice.stop()
        else:
            await ctx.send("I'm not playing anything!")


def setup(client):
    client.add_cog(Musicplayer(client))
