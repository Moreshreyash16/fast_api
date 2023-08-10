'''
@Author: Shreyash More

@Date: 2023-08-10 13:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-08-10 13:34:30

@Title : Create a simple crud operation api with api

'''
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()

API_KEY = os.getenv('ACCESS_TOKEN')

api_key_header = APIKeyHeader(name="access-token")

# function for authentication
async def authenticate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


app = FastAPI()
# creating a empty dictionary for storing data 
db={}

# creating a class item with basemodel as parameter
class Item(BaseModel):
    first_name:str
    last_name:str

# post operation
@app.post("/")
def create_data(item:Item,first:str,last:str,api_key: str = Depends(authenticate_api_key)):
    item.first_name=first
    item.last_name=last
    db[item.first_name]=item.last_name
    return{"Items":item}

# get operation 
@app.get("/")
def get_data(api_key: str = Depends(authenticate_api_key)):
    return db

# put operation
@app.put("/")
def update_data(item:Item,first:str,last:str):
    item.first_name=first
    item.last_name=last
    db[item.first_name]=item.last_name
    return db

# delete operation
@app.delete("/")
def delete_data(name:str):
    del db[name]
    return db

