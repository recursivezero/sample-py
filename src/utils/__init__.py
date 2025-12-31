from db.db_connection import mongo_client

if mongo_client:
  print("MongoDB connection successfull")