from pydantic import BaseModel
from fastapi import *
import uvicorn
import pymongo
import json
from fastapi.openapi.utils import get_openapi


# Studentinfo Class


class Studentinfo(BaseModel):
    roll_no: int
    name: str
    cl: str


# DATABASE CONNECTION
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["vikram"]
collection = db["studentinfo"]

# API CODE
api = FastAPI()

# CREATE OPRATION


@api.post("/enterstudentinfo",tags=["Endpoints"])
def enter_studentinfo(entry: Studentinfo):
    stdinfo = {"Roll No": entry.roll_no, "Name": entry.name, "Class": entry.cl}
    collection.insert_one(stdinfo)
    return {
        str("Stored 1 Record")

    }

# READ OPERATION


@api.get("/readstudentinfo",tags=["Endpoints"])
async def read_studentinfo(roll_no: int):
    data = collection.find_one({"Roll No": roll_no}, {"_id": False})
    try:
        return {
            "Roll No": data["Roll No"],
            "Name": data["Name"],
            "Class": data["Class"]
        }
    except:
        return {
            str("Something Went Wrong")
        }

# UPDATE OPERATION


@api.put("/updatestudentinfo",tags=["Endpoints"])
async def update_studentinfo(rno: int, dtu: Studentinfo):
    collection.update_one({"Roll No": rno}, {"$set": {"Roll No": dtu.roll_no, "Name": dtu.name, "Class": dtu.cl}})
    return {
        str("Updated 1 Record")
    }

# DELETE OPERATION


@api.delete("/deletestudentinfo",tags=["Endpoints"])
async def delete_studentinfo(roll_no: int):
    d = collection.delete_one({"Roll No": roll_no})
    return {
        str("Deleted 1 record")
    }

def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema
    openapi_schema = get_openapi(
        title="Student Management System API",
        version="1.0.0",
        description="Simple Rest API Made With FastAPI and MongoDB",
        routes=api.routes,
    )

    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    api.openapi_schema = openapi_schema
    return api.openapi_schema

api.openapi = custom_openapi


uvicorn.run(api, host="127.0.0.1", port=8000)
