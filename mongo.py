from pymongo import MongoClient

# Connect to MongoDB
mongo_client = MongoClient("mongodb://192.168.x.x:27017/")  # Replace with your actual IP
print("Connected to MongoDB successfully.")

# Select the database and collection
db = mongo_client["score_server"]  # Replace with actual database name
collection = db["user_models"]  # Replace with actual collection name

# List collections in the database
collections = db.list_collection_names()
print("Collections in MongoDB database:", collections)

# Retrieve and display a sample document
sample_doc = collection.find_one()
print("Sample document:", sample_doc)

# Query with a projection to limit fields (e.g., only "_id" and "name")
projected_doc = collection.find_one({}, {"_id": 1, "name": 1})  # Replace "name" with actual field name
print("Projected document:", projected_doc)