import discord, sys
from discord.ext import commands
sys.path.append("..")
from modules import Mongo, tools


class About(commands.Cog):
    """Bot Information"""

    def __init__(self, client):
        self.client = client
        self.MongoWorker = Mongo.MongoWorker()

    # commands
    @commands.command()
    async def info(self, ctx):
        command_prefix = self.client.command_prefix(self.client, ctx.message)
        embed = tools.embed_creator("Chadbot info", f" I'm a bot created by xxsuka#7765\n Server count: {len(self.client.guilds)}\n use {command_prefix}help to get help on the different bot categories and commands!", discord.Color.blue())
        await ctx.send("", embed = embed)
        await self.MongoWorker.add_misc("info", "info", ctx.message.author, ctx.message.guild)

    @commands.command(aliases=['invite'])
    async def inv(self, ctx):
        embed = tools.embed_creator("ChadBot Invite", "Invite me to your server! https://discord.com/api/oauth2/authorize?client_id=833176607496863804&permissions=67226688&scope=bot", discord.Color.blue())
        await ctx.send("", embed = embed)
        await self.MongoWorker.add_misc("inv", "inv", ctx.message.author, ctx.message.guild)

    @commands.command(aliases = ['chad'])
    @commands.has_permissions(embed_links=True)
    async def help(self, ctx, query=None):
        command_prefix = self.client.command_prefix(self.client, ctx.message)
        cogs_list = [c.capitalize() for c in self.client.cogs]
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
                description=f"These are all the command categories!\n Type {command_prefix}help [category] to get the list of commands from each category",
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
                  aliases_desc = ""
                  com_desc = com.name
                  for param in com.clean_params:
                    com_desc += f" <{param}>"
                  for alias in com.aliases:
                    aliases_desc += alias + " "
                  if aliases_desc == "":
                    commands_desc += f"{command_prefix}{com_desc}\n"
                  else:
                    commands_desc += f"{command_prefix}{com_desc} - Aliases: {aliases_desc}\n"
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
                embed = tools.embed_creator("ERROR", "Category not available!", discord.Color.red())
        await ctx.send("", embed=embed)
        await self.MongoWorker.add_misc("help", "help", ctx.message.author, ctx.message.guild)


async def setup(client):
    await client.add_cog(About(client))
