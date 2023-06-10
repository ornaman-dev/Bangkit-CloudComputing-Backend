from db.repository.users import create_new_user   # Import 'create_new_user' dari modul 'users' di dalam direktori db > repository untuk membuat user baru di basis data.
from db.session import get_db    # untuk memperoleh Session yang digunakan di berbagai environment (development, testing, production).
from fastapi import APIRouter   # Import 'APIRouter' class dari FastAPI untuk membuat router API.
from fastapi import Depends    # Import 'Depends' class dari FastAPI untuk menggunakan dependency yang diperlukan.
from schemas.users import ShowUser # Import skema 'ShowUser' dari modul 'users' di dalam direktori > schemas untuk validasi data yang dikirim ke endpoint. 
from schemas.users import UserCreate    # Import skema 'UserCreate' dari modul 'users' di dalam direktori > schemas untuk validasi data yang dikirim ke endpoint.
from sqlalchemy.orm import Session   # Import 'Session' dari SQLAlchemy untuk validasi tipe data sesi.

router = APIRouter() # Membuat objek router menggunakan APIRouter().

@router.post("/", response_model=ShowUser)   # Endpoint ini memiliki prefix '/user's dan tags ["users"] yang telah diatur di file base.py dalam direktori > apis. 
# Membuat fungsi create_user() sebagai handler untuk endpoint "Create User".
def create_user(user: UserCreate, db: Session = Depends(get_db)):    # Anotasi tipe 'UserCreate' untuk parameter user untuk memvalidasi data yang dikirim ke endpoint.
    user = create_new_user(user=user, db=db)
    return user
