from typing import TypedDict, Optional
from pymongo import MongoClient
from schema import Schema
from pymongo.collection import Collection
from define_schema import user_schema

class User:
    def __init__(self, id:str, name:str , value:int ):
        self.id = id
        self.name = name
        self.value = value
    def get(self):
        return self.id, self.name, self.value
    def insert(self):
        return (self.id, self.name, self.value)
    def update(self):
        return (self.name, self.value, self.id)


database = '9aidb'
connection_string = "mongodb://localhost:27017/" 
user = Schema(connection_string,database, user_schema,'users')
user._create_collection()
client = MongoClient(connection_string)
db = client[database]
collection = db['users']

users = User(collection)
#assests.insert({'_id': '5', 'name': 'assest2', 'value': 100})
users.insert({'_id': '2', 'name': 'assest3', 'value': 100})
#assests.insert({'_id': '7', 'name': 500, 'value': 100})
users.update({'_id': '2'}, {'$set': {'name': 'assest55'}})
client.close()
