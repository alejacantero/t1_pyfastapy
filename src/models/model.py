from typing import Optional 
from pydantic import BaseModel, EmailStr 

class TraineeModel(BaseModel):
    document:  str
    name: str 
    last_name: str
    email: EmailStr
    age: str 
    program: str
    record_number: int

class TraineeUpdateModel(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None 
    email: Optional[EmailStr]= None
    age: Optional[str] = None
    program: Optional[str] = None
    record_number: Optional[int] =None
    