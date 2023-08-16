from fastapi import APIRouter
from models.todos import Todo
from config.database import todos_collection
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


#GET Request Method 
@router.get('/', tags=['todos'])
async def get_todos():
    todos = list_serial(todos_collection.find())
    return todos

#POST Request Method 
@router.post('/', tags=['todos'])
async def post_todo(todo: Todo):
    todos_collection.insert_one(dict(todo))
    
    
#PUT Request Method 
@router.put('/{id}', tags=['todos'])
async def put_todo(id: str, todo: Todo):
    todos_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    
#DELETE Request Method 
@router.delete('/{id}', tags=['todos'])
async def delete_todo(id: str):
    todos_collection.find_one_and_delete({"_id": ObjectId(id)})
    