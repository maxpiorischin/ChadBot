from pymongo import MongoClient
import os
cluster = MongoClient(os.getenv("MONGODB_CONNECTION"), connect = False)
print(cluster)
db = cluster["ChadStats"]
commands = db["Commands"]

"""
post = { "_id": "img", "date": 2021, "content": "before stats", "user": "before stats" }
for i in range(1000):
    commands.insert_one(post)
"""
print(commands.find_one())