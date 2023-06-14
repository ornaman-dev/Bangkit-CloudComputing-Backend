from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class PlantBase(BaseModel):
    # class_name: Optional[str] = None
    # family_name: Optional[str] = None
    # common_name: Optional[str] = None
    # taxonomic_data_url: Optional[str] = None
    # location: Optional[str] = "Remote"
    # description: Optional[str] = None
    # date_posted: Optional[date] = datetime.now().date()
    # image_url: Optional[str] = None
    # light: Optional[str] = None
    # water: Optional[str] = None
    # humidity: Optional[str] = None
    # temperature: Optional[str] = None
    # food: Optional[str] = None
    # toxicity: Optional[str] = None
    # cares: Optional[str] = None
    # fact: Optional[str] = None
    # rec_id: Optional[str] = None
    
    id:Optional[str]
    name: Optional[str] 
    name_alt: Optional[str]
    image: Optional[str]
    desc: Optional[str] # desc
    light: Optional[str] # new rombak
    water: Optional[str] # new rombak
    humidity: Optional[str] # new rombak
    temperature: Optional[str] # new rombak
    food: Optional[str]  # new rombak
    toxicity: Optional[str] # new rombak
    cares: Optional[str] # new rombak
    fact: Optional[str] # new rombak


# this will be used to validate data while creating a Plant
class PlantCreate(PlantBase):
    class_name: str
    family_name: str
    location: str
    description: str


# this will be used to format the response to not to have id,fav_plant_id etc
class ShowPlant(PlantBase):
    # plant_id:int
    # class_name: str
    # family_name: str
    # taxonomic_data_url: Optional[str]
    # location: str
    # date_posted: date
    # description: Optional[str]
    # image_url: Optional[str]
    # light: Optional[str] = None
    # water: Optional[str] = None
    # humidity: Optional[str] = None
    # temperature: Optional[str] = None
    # food: Optional[str] = None
    # toxicity: Optional[str] = None
    # cares: Optional[str] = None
    # fact: Optional[str] = None
    # rec_id: Optional[str] = None

    id: str
    name: str
    name_alt: str
    image: Optional[str]
    desc: Optional[str] # desc
    light: Optional[str] # new rombak
    water: Optional[str] # new rombak
    humidity: Optional[str] # new rombak
    temperature: Optional[str] # new rombak
    food: Optional[str]  # new rombak
    toxicity: Optional[str] # new rombak
    cares: Optional[str] # new rombak
    fact: Optional[str] # new rombak

    class Config:  # to convert non dict obj to json
        orm_mode = True
