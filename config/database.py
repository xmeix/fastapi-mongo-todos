from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://xmeix:xmeix911@cluster0.zhtofdq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)


db = client.todo_database

todos_collection = db["todos"]
users_collection = db["users"]
