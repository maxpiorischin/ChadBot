from pymongo import MongoClient
import os
cluster = MongoClient(os.getenv("MONGODB_CONNECTION"), connect = False)
print(cluster)
db = cluster["ChadStats"]
commands = db["Commands"]

commands.renameCollection("IMG")