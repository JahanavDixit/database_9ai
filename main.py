from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from connect import *

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

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/get/{collection}")
async def get(collection: str):
    return {"collection": collection}

@app.post("/insert/{collection}")
async def insert(collection: str):
    return {"collection": collection}

@app.post("/update/{collection}")
async def update(collection: str):
    return {"collection": collection}