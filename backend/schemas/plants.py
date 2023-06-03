from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class PlantBase(BaseModel):
    class_name: Optional[str] = None
    family_name: Optional[str] = None
    common_name: Optional[str] = None
    taxonomic_data_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()
    image_url: Optional[str] = None


# this will be used to validate data while creating a Plant
class PlantCreate(PlantBase):
    class_name: str
    family_name: str
    location: str
    description: str


# this will be used to format the response to not to have id,fav_plant_id etc
class ShowPlant(PlantBase):
    class_name: str
    family_name: str
    taxonomic_data_url: Optional[str]
    location: str
    date_posted: date
    description: Optional[str]
    image_url: Optional[str]

    class Config:  # to convert non dict obj to json
        orm_mode = True
