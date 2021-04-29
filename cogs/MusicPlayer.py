import discord
from discord.ext import commands
import sys
import os
import asyncio

sys.path.append("..")
from modules import ytVideoGrabber
import youtube_dl


class Musicplayer(commands.Cog):
    """Playing Music in a voice channel"""

    def __init__(self, client):
        self.client = client

    # commands

    @commands.command()
    async def play(self, ctx, *search):
        search_term = '+'.join(search)
        link = ytVideoGrabber.videograbber(search_term)
        voiceChannel = ctx.message.author.voice.channel
        await voiceChannel.connect()
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                voice.play(discord.FFmpegPCMAudio(file))
                os.remove("./" + file)
    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Currently no audio is playing.")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("The audio is not paused.")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()

"""def setup(client):
    client.add_cog(Musicplayer(client)) """
