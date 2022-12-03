from discord.ext import commands
import requests
from urllib.parse import quote


class MultiString(commands.Converter):
    def __init__(
        self,
        n=2,
        require=False,
        fill_missing=False,
    ):
        self.n = n
        self.require = require
        self.fill_missing = fill_missing

    async def convert(self, ctx: commands.Context, argument: str) -> list:
        args = argument.replace(", ", ",").replace(" ,", ",").split(",")
        if not isinstance(args, list):
            args = [args]

        args = args[: self.n]
        if not self.fill_missing:
            if self.require and len(args) != self.n:
                raise commands.UserInputError()
        else:
            diff = self.n - len(args)
            args += ["" for _ in range(diff)]

        parsed = []
        for arg in args:
            parsed.append(
                await commands.clean_content(
                    use_nicknames=True, fix_channel_mentions=True
                ).convert(ctx, arg)
            )

        return parsed[: self.n]


class Mimes(commands.Cog):
    """Mime memes"""

    def __init__(self, bot):
        self.bot = bot

        self.memes = "all"
        self.memes_data = None
        self.base_url = "https://mime.rcp.r9n.co/memes"

    def to_query_string(self, fields: dict) -> str:
        return "&".join(f"{k}={quote(v)}" for k, v in fields.items())

    def add_meme_commands(self):
        resp = requests.post("https://mime.rcp.r9n.co/multidocs", json=self.memes)
        self.memes_data = {
            k: v for k, v in resp.json().items() if "image" not in v.values()
        }

        for meme_id, meme_fields in self.memes_data.items():

            @commands.command(
                name=meme_id,
                help=f'{", ".join(f"<k>" for k in meme_fields.keys())} sends a meme',
            )
            @commands.bot_has_permissions(embed_links=True)
            async def cmd(self, ctx, *, content: MultiString(n=5, fill_missing=True)):
                fields = self.to_query_string(
                    {
                        k: v
                        for k, v in zip(
                            self.memes_data[ctx.command.name].keys(),
                            content[: len(self.memes_data[ctx.command.name])],
                        )
                    }
                )

                embed = (
                    discord.Embed(color=discord.Color.random())
                    .set_image(url=f"{self.base_url}/{ctx.command.name}?{fields}")
                    .set_footer(text="made with mime")
                )
                await ctx.reply(embed=embed)

            cmd.cog = self
            self.__cog_commands__ = self.__cog_commands__ + (cmd,)
            self.bot.add_command(cmd)


async def setup(bot):
    cog = Mimes(bot)
    await bot.add_cog(cog)
    cog.add_meme_commands()
