import discord
import os
import random


def embed_creator(title, desc, colour):
    embed = discord.Embed(title=title, description=desc, color=colour)
    return embed


def pastel_color():
    rgb = [100, random.randint(100, 237), 237]
    random.shuffle(rgb)
    return tuple(rgb)


async def quick_embed(ctx, reply=True, delete_image=True, send=True, **kwargs):
    title = kwargs.get("title", "")
    description = kwargs.get("description", "")
    timestamp = kwargs.get("timestamp")
    color = kwargs.get("color", discord.Color.from_rgb(*pastel_color()))
    thumbnail = kwargs.get("thumbnail")
    author = kwargs.get("author")
    footer = kwargs.get("footer", {})
    fields = kwargs.get("fields")
    image = kwargs.get("image")
    bimage = kwargs.get("bimage")
    image_url = kwargs.get("image_url", "")
    url = kwargs.get("url", "")
    stats = kwargs.get("stats")

    embed = discord.Embed(title=title, description=description, color=color, url=url)
    if timestamp:
        embed.timestamp = timestamp

    file = None
    if not image_url:
        if bimage:
            embed.set_image(url=f"attachment://bytesimage.jpg")
            file = discord.File(fp=bimage, filename="bytesimage.jpg")
        elif image:
            filename = os.path.basename(image)
            embed.set_image(url=f"attachment://{filename}")
            file = discord.File(fp=image, filename=filename)
    else:
        embed.set_image(url=image_url)

    if thumbnail:
        embed.set_thumbnail(url=thumbnail)

    if author:
        embed.set_author(
            name=author.get("name", "\u200b"),
            url=author.get("url", ""),
            icon_url=author.get("icon_url", ""),
        )

    if footer or stats:
        text = footer.get("text", "")
        if text and stats:
            text += " • "
        embed.set_footer(
            text=text + (f"{ctx.prefix}{ctx.command.name} • {stats}" if stats else ""),
            icon_url=footer.get("icon_url", ""),
        )

    if fields:
        for f in fields:
            embed.add_field(
                name=f.get("name", "\u200b"),
                value=f.get("value", "\u200b"),
                inline=f.get("inline", True),
            )

    if send:
        if reply:
            msg = await ctx.reply(file=file, embed=embed, mention_author=False)
        else:
            msg = await ctx.send(file=file, embed=embed)

    if delete_image and image:
        os.remove(image)

    if send:
        return msg
    else:
        return embed
