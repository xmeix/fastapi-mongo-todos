from fastapi import APIRouter
from models.todos import Todo
from config.database import users_collection
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


#GET Request Method 
@router.get('/', tags=['users'])
async def get_users():
    users = list_serial(users_collection.find())
    return users
