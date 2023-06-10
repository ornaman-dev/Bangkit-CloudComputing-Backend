from db.models.favorite import Favorite
from schemas.favorite import AddFavoritePlant
from sqlalchemy.orm import Session


def add_new_favorite_plant(favorite: AddFavoritePlant, db: Session, fav_id: int):
    favorite_object = Favorite(**favorite.dict(), fav_id=fav_id)
    db.add(favorite_object)
    db.commit()
    db.refresh(favorite_object)
    return favorite_object