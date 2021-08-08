from pymongo import MongoClient
import os
cluster = MongoClient(os.getenv("MONGODB_CONNECTION"), connect = False)
print(cluster)
db = cluster["ChadStats"]
IMG = db["IMG"]
Misc = db["Misc"]
WebSearch = db["WebSearch"]
Youtube = db["Youtube"]

for i in range(2800):
    post = {"_id": "img" + str(i), "command": "img", "date": 2021, "content": "before stats", "user": "before stats"}
    IMG.insert_one(post)

for i in range(600):
    post = {"_id": "misc" + str(i), "command": "misc", "date": 2021, "content": "before stats", "user": "before stats"}
    Misc.insert_one(post)

for i in range(100):
    post = {"_id": "yt" + str(i), "command": "yt", "date": 2021, "content": "before stats", "user": "before stats"}
    Youtube.insert_one(post)

for i in range(130):
    post = {"_id": "search" + str(i), "command": "define", "date": 2021, "content": "before stats", "user": "before stats"}
    WebSearch.insert_one(post)

print("done")