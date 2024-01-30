from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from connect import *
from assistant import Assistant
from assests import Assest
from session import Session
from channel import Channel
from tenant import Tenant
from thread_col import Thread_col
from user import User
from threading import Thread
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


connection_string = 'mongodb://localhost:27017/'
client = MongoClient(connection_string)
db = client['9aidb']

COLLECTION_MAPPING = {
    "assistants": Assistant,
    "assests": Assest,
    "sessions": Session,
    "channels": Channel,
    "tenants": Tenant,
    "users": User,
    "threads": Thread_col
}


@app.get("/")
async def read_root():
    return "PyMongo API"

@app.get("/get/{collection}/{id}")
async def get(collection: str,id:str):
    data_class = COLLECTION_MAPPING.get(collection.lower())
    data_obj = data_class(db[collection.lower()])
    return data_obj.get({'id':id})

@app.post("/insert/{collection}/")
async def insert(collection: str,data: dict):
    data_class = COLLECTION_MAPPING[collection.lower()]
    data_obj = data_class(db[collection.lower()])
    data_obj.insert(data)
    return "Success"

@app.post("/update/{collection}")
async def update(collection: str,data: dict,id:str):
    data_class = COLLECTION_MAPPING[collection.lower()]
    data_obj = data_class(db[collection.lower()])
    data_obj.update({'_id': id}, {'$set': data})
    return "Success"