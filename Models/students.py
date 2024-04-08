from pydantic import BaseModel


class addressSchema(BaseModel):
    city:str
    country:str


class studentSchema(BaseModel):
    name:str
    age:int
    address:addressSchema