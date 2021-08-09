from pymongo import MongoClient
import os
from datetime import datetime
import time
cluster = MongoClient(os.getenv("MONGODB_CONNECTION"), connect = False)
print(cluster)
db = cluster["ChadStats"]
IMG = db["IMG"]
Misc = db["Misc"]
WebSearch = db["WebSearch"]
Youtube = db["Youtube"]

for i in range(2810):
    post = {"_id": datetime.now(), "command": "b4stat", "date": 2021, "content": "before stats", "user": "before stats"}
    IMG.insert_one(post)

for i in range(600):
    post = {"_id": datetime.now(), "command": "b4stat", "date": 2021, "content": "before stats", "user": "before stats"}
    Misc.insert_one(post)

for i in range(100):
    post = {"_id": datetime.now(), "command": "b4stat", "date": 2021, "content": "before stats", "user": "before stats"}
    Youtube.insert_one(post)

for i in range(130):
    post = {"_id": datetime.now(), "command": "b4stat", "date": 2021, "content": "before stats", "user": "before stats"}
    WebSearch.insert_one(post)

print("done")

time.sleep(30)