# from typing import Optional # not yet used
from pydantic import BaseModel
from pydantic import EmailStr


# properties required during user creation
class UserCreate(BaseModel):
    username: str  # TODO ganti jadi name atau full_name
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    username: str  # TODO ganti jadi name atau full_name
    email: EmailStr
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
