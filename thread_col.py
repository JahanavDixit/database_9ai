from typing import TypedDict, Optional
from pymongo import MongoClient
from schema import Schema
from pymongo.collection import Collection
from connect import thread_schema

class Thread_col:
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
thread = Schema(connection_string,database, thread_schema,'threads')
thread._create_collection()