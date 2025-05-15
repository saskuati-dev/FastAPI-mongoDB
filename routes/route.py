from fastapi import APIRouter

from models.todos import Todo
from config.database import colecao
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

#GET request

@router.get('/')
async def get_todos():
    todos = list_serial(colecao.find())
    return todos

#POST request
@router.post('/')
async def post_todo(todo: Todo):
    colecao.insert_one(dict(todo))


#PUT request
@router.put('/{id}')
async def put_todo(id: str, todo: Todo):
    colecao.find_one_and_update({'_id': ObjectId(id)}, {'$set': dict(todo)})

#DELETE request
@router.delete('/{id}')
async def delete_todo(id:str):
    colecao.find_one_and_delete({'_id': ObjectId(id)})