import discord


def embed_creator(title, desc, colour):
    embed = discord.Embed(
        title=title,
        description=desc,
        color=colour
    )
    return embed
