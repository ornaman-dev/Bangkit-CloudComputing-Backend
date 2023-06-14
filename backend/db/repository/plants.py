# db > repository > plants.py
from db.models.plants import Plants
from schemas.plants import PlantCreate
from sqlalchemy.orm import Session


def create_new_plant(plant: PlantCreate, db: Session, fav_plant_id: int):
    plant_object = Plant(**plant.dict(), fav_plant_id=fav_plant_id)
    db.add(plant_object)
    db.commit()
    db.refresh(plant_object)
    return plant_object


def retreive_plant(id: str, db: Session):
    item = db.query(Plants).filter(Plants.id == id).first()
    # It is equivalent to sql command: select * from plant where plant_id = {plant_id};
    return item


def list_plants(db: Session):
    # plants = db.query(Plant).filter(Plant.is_active == True).all()
    plants = db.query(Plants).all()
    return plants


def search_plant(query: str, db: Session):
    plants = db.query(Plants).filter(Plants.class_name.contains(query))
    return plants


def update_plant_by_id(plant_id: int, plant: PlantCreate, db: Session, fav_plant_id):
    existing_plant = db.query(Plants).filter(Plants.plant_id == plant_id)
    if not existing_plant.first():
        return 0
    plant.__dict__.update(
        fav_plant_id=fav_plant_id
    )  # update dictionary with new key value of fav_plant_id
    existing_plant.update(plant.__dict__)
    db.commit()
    return 1


def delete_plant_by_id(plant_id: int, db: Session, fav_plant_id):
    existing_plant = db.query(Plants).filter(Plants.plant_id == plant_id)
    if not existing_plant.first():
        return 0
    existing_plant.delete(synchronize_session=False)
    db.commit()
    return 1
