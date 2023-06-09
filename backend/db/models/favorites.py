from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String


class Favorite(Base):
    fav_id = Column(String, primary_key=True, index=True)
    user_fav_id = Column(String, ForeignKey("user.id"))
    plant_fav_id = Column(String, ForeignKey("plant.plant_id"))