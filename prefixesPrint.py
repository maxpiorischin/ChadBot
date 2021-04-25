from replit import db

keys = db.keys()
for key in keys:
  print(f"Discord id:{key} Prefix: {db[key]}")