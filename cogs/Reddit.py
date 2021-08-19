import discord, asyncpraw
from discord.ext import commands
import sys
import os

sys.path.append("..")
from modules import LinkGrabber, tools, Mongo
reddit_id = os.getenv("reddit_id")
reddit_secr_id = os.getenv("reddit_secr_id")
user_agent = os.getenv("reddit_user_agent")

class Reddit(commands.Cog):
    """Reddit Commands"""

    def __init__(self, client):
        self.client = client
        self.reddit = asyncpraw.Reddit(
            client_id=reddit_id,
            client_secret=reddit_secr_id,
            user_agent=user_agent,
        )
        self.MongoWorker = Mongo.MongoWorker()


    # commands
    @commands.command(aliases=["subreddit", "r"])
    async def reddit(self, ctx, *search):
        search_term = ''.join(search)
        print("searching reddit: " + search_term)
        last_val = search_term[len(search_term.rstrip('0123456789')):]
        if not last_val.isdigit():
            last_val = 1
        if int(last_val) > 10:
            embed = tools.embed_creator("ERROR", "Maximum of 10 Images!", discord.Color.red())
            await ctx.send("", embed=embed)
            return
        if (search_term.endswith("," + last_val)) and 0 < int(last_val) <= 10:
            search_term = search_term[:-(len(last_val) + 2)]
            print(search_term)
            try:
                subreddit = await self.reddit.subreddit(search_term)
                async for submission in subreddit.hot(limit=last_val):
                    await ctx.send(submission.title)
            except:
                embed = tools.embed_creator("ERROR", "Subreddit does not exist", discord.Color.red())
                await ctx.send("", embed = embed)
        await self.MongoWorker.add_reddit("reddit", search_term, ctx.message.author, ctx.message.guild)



def setup(client):
    client.add_cog(Reddit(client))