import discord
from discord.ext import commands
from replit import db


class About(commands.Cog):
    """Bot Information"""

    def __init__(self, client):
        self.client = client

    # commands
    @commands.command()
    async def info(self, ctx):
        await ctx.send("``` I'm a bot created by xxsuka#7765\n Server count: {} ```".format(len(self.client.guilds)))

    @commands.command()
    @commands.has_permissions(embed_links=True)
    async def help(self, ctx, query=None):
        command_prefix = self.client.command_prefix(self.client, ctx.message)
        cogs_list = [c for c in self.client.cogs]
        cogs_desc = ""
        commands_desc = ""
        private_cogs = ['Fortnut']
        embed = ""
        if query is None:
            for cog in self.client.cogs:
                if cog not in private_cogs:
                    cogs_desc += f"`{cog}` - {self.client.cogs[cog].__doc__}\n"

            embed = discord.Embed(
                title="ChadBot Help",
                description=f"These are all the command categories!\n Type {command_prefix}help[category] to get the list of commands from each category",
                color=discord.Color.blue()
            )

            embed.add_field(
                name="categories",
                value=cogs_desc,
                inline=False
            )
        else:
            if query.capitalize() in cogs_list:
                cog_commands = self.client.get_cog(query.capitalize()).get_commands()
                for com in cog_commands:
                    commands_desc += f"`{com}`"
                embed = discord.Embed(
                    title="ChadBot Help",
                    description=f"These are all the commands for category {query}!\n",
                    color=discord.Color.blue()
                )

                embed.add_field(
                    name="Commands",
                    value=commands_desc,
                    inline=False
                )
            else:
                await ctx.send("Category not available!")
        await ctx.send("", embed=embed)


def setup(client):
    client.add_cog(About(client))
