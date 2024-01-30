from typing import TypedDict, Optional
from pymongo import MongoClient
from schema import Schema
from pymongo.collection import Collection
from define_schema import session_schema

class Session:
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
session = Schema(connection_string,database, session_schema,'sessions')
session._create_collection()
client = MongoClient(connection_string)
db = client[database]
collection = db['sessions']

sessions = Session(collection)
#assests.insert({'_id': '5', 'name': 'assest2', 'value': 100})
sessions.insert({'_id': '2', 'name': 'assest3', 'value': 100})
#assests.insert({'_id': '7', 'name': 500, 'value': 100})
sessions.update({'_id': '2'}, {'$set': {'name': 'assest55'}})
client.close()
