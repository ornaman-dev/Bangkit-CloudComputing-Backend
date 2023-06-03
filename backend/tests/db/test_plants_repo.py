# > tests > db > test_plants_repo.py
from sqlalchemy.orm import Session 

from db.repository.plants import create_new_plant,retreive_plant
from schemas.plants import PlantCreate
from tests.utils.users import create_random_fav_by


def test_retreive_plant_by_id(db_session:Session):
    class_name = "test english name"
    family_name = "family ornaman"
    common_name = "common ornaman"
    taxonomic_data_url = "ornaman.test"
    location = "Indonesia"
    description = "desc Ornaman"
    fav_by = create_random_fav_by(db=db_session)
    plant_schema = PlantCreate(class_name=class_name,family_name=family_name,common_name=common_name,taxonomic_data_url=taxonomic_data_url,
    location=location,description=description)
    plant = create_new_plant(plant=plant_schema, db=db_session, fav_plant_id=fav_by.id)
    retreived_plant = retreive_plant(plant_id=plant.plant_id,db=db_session)
    assert retreived_plant.plant_id == plant.plant_id 
    assert retreived_plant.class_name == "test english name"

    