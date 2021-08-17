from pymongo import MongoClient
import motor
import motor.motor_asyncio
import os, sys
from datetime import date, datetime

class MongoWorker:
    def __init__(self):
        self.cluster = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_CONNECTION"))
        self.dbchad = self.cluster["Chad"]
        self.prefixes = self.dbchad["Prefixes"]
        self.dbchadstats = self.cluster["ChadStatsLive"]
        self.IMG = self.dbchadstats["IMG"]
        self.Misc = self.dbchadstats["Misc"]
        self.WebSearch = self.dbchadstats["WebSearch"]
        self.Youtube = self.dbchadstats["Youtube"]

    async def get_prefix(self, message):
        post = self.prefixes.find_one({"_id": str(message.guild.id)})
        return post["prefix"]

    async def add_prefix(self, id, prefix):
        post = {"_id": str(id), "prefix": prefix}
        self.prefixes.insert_one(post)

    async def del_prefix(self, id):
        self.prefixes.delete_one({"_id": str(id)})

    async def update_prefix(self, id, prefix):
        self.prefixes.update_one({"_id": str(id)}, {"$set": {"prefix": prefix}})

    async def add_img(self, content, user):
        post = {"_id": datetime.now(), "command": "img", "content": content,
                "user": user.name + "#" + user.discriminator, "time" : str(date.today())}
        self.IMG.insert_one(post)
    async def add_misc(self, command, content, user):
        post = {"_id": datetime.now(), "command": command,"content": content,
                "user": user.name + "#" + user.discriminator, "time" : str(date.today())}
        self.Misc.insert_one(post)
    async def add_web(self, command, content, user):
        post = {"_id": datetime.now(), "command": command, "content": content,
                "user": user.name + "#" + user.discriminator, "time" : str(date.today())}
        self.WebSearch.insert_one(post)
    async def add_youtube(self, command, content, user):
        post = {"_id": datetime.now(), "command": command, "content": content,
                "user": user.name + "#" + user.discriminator, "time" : str(date.today())}
        self.Youtube.insert_one(post)
