# tests > utils > users.py
import random
import string

from db.repository.users import create_new_user
from db.repository.users import get_user_by_email
from fastapi.testclient import TestClient
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def create_random_fav_by(db: Session):
    email = f"{random_lower_string()}@{random_lower_string()}.com"
    password = random_lower_string()
    id_rec = f"{random_lower_string()}-"
    user_schema = UserCreate(
        email=email, password=password, id_rec=id_rec
    )
    user = create_new_user(user=user_schema, db=db)
    return user


def user_authentication_headers(
    client: TestClient, email: str, password: str, id_rec: str
):
    """
    Mendapatkan header otentikasi pengguna berdasarkan email dan password.
    """
    # Implementasi logika untuk mendapatkan header otentikasi
    # menggunakan email, password, dan id_rec
    data = {"email": email, "password": password}
    r = client.post("/login/token", data=data)
    response = r.json()
    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers  # Kembalikan headers sesuai kebutuhan


def authentication_token_from_email(client: TestClient, email: str, db: Session):
    """
    Mengembalikan token valid untuk pengguna dengan email tertentu.
    Jika pengguna belum ada, pengguna akan dibuat terlebih dahulu.
    """
    password = "random-passW0rd"
    id_rec = "contoh_id_rec"  # Definisikan variabel id_rec di sini
    user = get_user_by_email(email=email, db=db)
    if not user:
        # Jika pengguna tidak ditemukan, buat pengguna baru dengan email tersebut
        user_in_create = UserCreate(
            name=email, email=email, password=password
        )
        user = create_new_user(user=user_in_create, db=db)
    else:
        # Jika pengguna ditemukan, perbarui nilai id_rec
        id_rec = user.id_rec
    return user_authentication_headers(
        client=client, email=email, password=password, id_rec=id_rec
    )
