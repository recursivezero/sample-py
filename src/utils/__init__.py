from db.connection import mongo_client

if mongo_client:
  print("MongoDB connected successfully.")