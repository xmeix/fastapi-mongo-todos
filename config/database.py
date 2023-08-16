import motor.motor_asyncio

uri = "mongodb+srv://xmeix:xmeix911@cluster0.zhtofdq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = motor.motor_asyncio.AsyncIOMotorClient(uri)


db = client.todo_database

todos_collection = db["todos"]
users_collection = db["users"]


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You have successfully connected to MongoDB!")
except Exception as e:
    print(e)