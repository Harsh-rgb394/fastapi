from fastapi import APIRouter
from Models.students import studentSchema
from config.db import collection_name
from Schemas.studentSchema import getallitems,singleitem
from bson import ObjectId


router=APIRouter()
@router.head("/")
async def head_route():

    return {"X-Custom-Header": "Value"} 

# for default pages 
# @router.get("/")
# async def defautl_route():
#     return {"student mangement library"}

# for get all students 
@router.get("/students")
async def get_students(country: str,age:int):
    query={}

    if country:
        # students_data=collection_name.find({"address.country":country})
        query["address.country"]=country
    
    if age:
        # students_data=collection_name.find()
        query["age"]={"$gte":age}

    students_data=collection_name.find(query)
    
    students=getallitems(students_data)
    return students


# for creating the new student 
@router.post("/students")
async def create_students(studentSchema:studentSchema):

    address_data = dict(studentSchema.address)
    student_data = dict(studentSchema)
    student_data["address"] = address_data

    result = collection_name.insert_one(student_data) 

    if result.acknowledged:

        return{
            "Description": "Student created successfully",
            "StudentID": str(result.inserted_id)
        }


# for updating the new student 
@router.put("/students/{id}")
async def update_students(id:str,studentSchema:studentSchema):
    address_data = dict(studentSchema.address)
    student_data = dict(studentSchema)
    student_data["address"] = address_data
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(student_data)}) 


# for geeting single student 
@router.get("/students/{id}")
async def getone_student(id:str):
    student=collection_name.find_one({"_id":ObjectId(id)})
    student=singleitem(student)
    return student

# for deleting the student 
@router.delete("/students/{id}")
async def delete_student(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
