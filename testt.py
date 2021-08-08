from pymongo import MongoClient
import os
cluster = MongoClient(os.getenv("MONGODB_CONNECTION"), connect = False)
print(cluster)
db = cluster["ChadStats"]
commands = db["Commands"]

for i in range(2800):
    post = {"_id": "img" + str(i), "command": "img", "date": 2021, "content": "before stats", "user": "before stats"}
    commands.insert_one(post)

print("done")