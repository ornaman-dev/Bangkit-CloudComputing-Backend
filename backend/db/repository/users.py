# db > repository > users.py
from core.hashing import Hasher
from db.models.users import Users
from schemas.users import UserCreate
from sqlalchemy.orm import Session


def create_new_user(user: UserCreate, db: Session):
    # Membuat user baru berdasarkan data yang diberikan
    user = Users(
        id=user.id,
        name=user.name,  # TODO ganti jadi name atau full_name
        email=user.email,
        password=user.password
    )
        # hashed_password=Hasher.get_password_hash(user.password),
        # is_active=True,
        # is_superuser=False,
        # id_rec=user.id_rec,
    # Menambahkan user baru ke sesi basis data
    db.add(user)
    # Melakukan komit ke basis data untuk menyimpan perubahan
    db.commit()
    # Memperbarui objek user dengan data yg disimpan di basis data
    db.refresh(user)
    # Mengembalikan objek user yang baru dibuat
    return user


def get_user_by_email(email: str, db: Session):
    # Mengambil user berdasarkan alamat email
    user = db.query(User).filter(User.email == email).first()
    # Mengembalikan objek user yang ditemukan (jika ada)
    return user


def list_users(db: Session):
    """
    Mengembalikan daftar semua user yang aktif dari database.
    """
    users = db.query(User).filter(User.is_active == True).all()
    return users


def retreive_user(id: int, db: Session):
    """
    Mengembalikan data user berdasarkan ID yang diberikan dari database.
    """
    item = db.query(User).filter(User.id == id).first()
    # Ini ekuivalen dengan perintah SQL: select * from user where id = {id};
    return item
