from db.models.plants import Plant
from schemas.plants import PlantCreate
from sqlalchemy.orm import Session


def create_new_plant(plant: PlantCreate, db: Session, fav_plant_id: int):
    plant_object = Plant(**plant.dict(), fav_plant_id=fav_plant_id)
    db.add(plant_object)
    db.commit()
    db.refresh(plant_object)
    return plant_object


def retreive_plant(plant_id: int, db: Session):
    item = (
        db.query(Plant).filter(Plant.plant_id == plant_id).first()
    )  # It is equivalent to sql command: select * from plant where plant_id = 1;
    return item
