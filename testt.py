from pymongo import MongoClient
import os
cluster = MongoClient(os.getenv("MONGODB_CONNECTION"), connect = False)
print(cluster)
db = cluster["ChadStats"]
commands = db["Commands"]

post = { "command": "img", "date": 2021, "content": "before stats", "user": "before stats" }
for i in range(2800):
    commands.insert_one(post)

print("done")