from typing import TypedDict, Optional
from pymongo import MongoClient
from schema import Schema
from pymongo.collection import Collection
from connect import session_schema

class Session:
    def __init__(self, collection: Collection):
        self.collection = collection

    def get(self, query):
        return self.collection.find_one(query)

    def insert(self, data: TypedDict):
        return self.collection.insert_one(data)

    def update(self, query, update_data):
        return self.collection.update_one(query, update_data)



database = '9aidb'
connection_string = "mongodb://localhost:27017/" 
session = Schema(connection_string,database, session_schema,'sessions')
session._create_collection()
# client = MongoClient(connection_string)
# db = client[database]
# collection = db['sessions']

# sessions = Session(collection)
# #assests.insert({'_id': '5', 'name': 'assest2', 'value': 100})
# sessions.insert({'_id': '2', 'name': 'assest3', 'value': 100})
# #assests.insert({'_id': '7', 'name': 500, 'value': 100})
# sessions.update({'_id': '2'}, {'$set': {'name': 'assest55'}})
# client.close()
