from fastapi import APIRouter, HTTPException, status, Body
from models.users import User, UserLogin
from config.database import users_collection
from schema.schemas import list_serial, individual_serial_user
from bson import ObjectId
from controllers.auth.jwt_handler import generateJWT
import asyncio

router = APIRouter()
 


@router.post('/user/',tags=['user'])
async def register_user(user: User):
    try:
        user = dict(user)
        result = await users_collection.insert_one(user)
        print(result.inserted_id)
    except Exception as e:
        print(e)
    return {"message": "Success"}
 
