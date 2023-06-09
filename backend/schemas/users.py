# > schemas > users.py
# from typing import Optional # modul ini belum digunakan
from pydantic import BaseModel
from pydantic import EmailStr


# Properti yang diperlukan saat membuat User baru
class UserCreate(BaseModel):
    username: str  # TODO ganti jadi name atau full_name
    email: EmailStr
    password: str
    id_rec: str


class ShowUser(BaseModel):
    username: str  # TODO ganti jadi name atau full_name
    email: EmailStr
    is_active: bool
    # id_rec: str

    class Config:  # memberi tahu pydantic untuk mengonversi objek non-dictionary menjadi json
        orm_mode = True
