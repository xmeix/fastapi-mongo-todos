from fastapi import APIRouter
from models.todos import Todo
from config.database import todos_collection
from schema.schemas import list_serial, individual_serial_todo
from bson import ObjectId

router = APIRouter()

#GET Request Method 
@router.get('/todos', tags=['todos'])
async def get_todos():
    todos = list_serial(todos_collection.find(),individual_serial_todo)
    return todos


#POST Request Method 
@router.post('/todos', tags=['todos'])
async def post_todo(todo: Todo):
    todos_collection.insert_one(dict(todo))
    
    
#PUT Request Method 
@router.put('/todos/{id}', tags=['todos'])
async def put_todo(id: str, todo: Todo):
    todos_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    
#DELETE Request Method 
@router.delete('/todos/{id}', tags=['todos'])
async def delete_todo(id: str):
    todos_collection.find_one_and_delete({"_id": ObjectId(id)})
    