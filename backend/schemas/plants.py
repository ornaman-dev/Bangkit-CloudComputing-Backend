from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class PlantBase(BaseModel):
    english_name: Optional[str] = None
    family_name: Optional[str] = None
    common_name: Optional[str] = None
    wikipedia_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


# this will be used to validate data while creating a Plant
class PlantCreate(PlantBase):
    english_name: str
    family_name: str
    location: str
    description: str


# this will be used to format the response to not to have id,fav_plant_id etc
class ShowPlant(PlantBase):
    english_name: str
    family_name: str
    wikipedia_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
