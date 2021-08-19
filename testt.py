import discord, asyncpraw, asyncio
from discord.ext import commands
import sys
import os
reddit_id = "1opDI8rNa3mnyQzxIKMShg"
reddit_secr_id = "ZFI6wVekzRF3PGUatCxoFBAWIfgcXQ"
user_agent = "maxboss2002"

reddit = asyncpraw.Reddit(
            client_id=reddit_id,
            client_secret=reddit_secr_id,
            user_agent=user_agent,
        )

print(reddit.read_only)