from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['todo-database']

colecao = db['todos']
