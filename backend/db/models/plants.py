from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Plant(Base):
    plant_id = Column(Integer, primary_key=True, index=True)  # plant_id
    english_name = Column(String, nullable=False)
    family_name = Column(String, nullable=False)  # family_name
    common_name = Column(String, nullable=False)  # common_name
    wikipedia_url = Column(String)  # wikipedia_url
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    fav_plant_id = Column(Integer, ForeignKey("user.id"))
    pav_by = relationship("User", back_populates="fav_plant")
