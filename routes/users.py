from fastapi import APIRouter, HTTPException, status
from models.todos import Todo
from config.database import users_collection
from schema.schemas import list_serial, individual_serial_user
from bson import ObjectId
 
 
router = APIRouter()




#GET Request Method 
@router.get('/users', tags=['users'])
async def get_users():
    users = list_serial(users_collection.find(),individual_serial_user)
    return users
