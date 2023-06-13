# apis > version1 > route_plants.py
from typing import List  # for list view
from typing import Optional

from apis.version1.route_login import get_current_user_from_token
from db.models.users import Users
from db.repository.plants import create_new_plant
from db.repository.plants import delete_plant_by_id
from db.repository.plants import list_plants
from db.repository.plants import retreive_plant
from db.repository.plants import search_plant
from db.repository.plants import update_plant_by_id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.plants import PlantCreate
from schemas.plants import ShowPlant
from sqlalchemy.orm import Session


router = APIRouter()


@router.get("/autocomplete")
def autocomplete(term: Optional[str] = None, db: Session = Depends(get_db)):
    plants = search_plant(term, db=db)
    plant_class_names = []
    for plant in plants:
        plant_class_names.append(plant.class_name)
    return plant_class_names


@router.post("/create-plant/", response_model=ShowPlant)
def create_plant(
    plant: PlantCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user_from_token),
):
    fav_plant_id = current_user.id
    plant = create_new_plant(plant=plant, db=db, fav_plant_id=fav_plant_id)
    return plant


# function retreive plant dari database
@router.get("/get/{plant_id}", response_model=ShowPlant)
def read_plant(plant_id: int, db: Session = Depends(get_db)):
    plant = retreive_plant(plant_id=plant_id, db=db)
    if not plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plant with this id {plant_id} does not exist",
        )
    return plant


@router.get("/all", response_model=List[ShowPlant])  # for list view
def read_plants(db: Session = Depends(get_db)):
    plants = list_plants(db=db)
    return plants


@router.put("/update/{plant_id}")  # update plant
def update_plant(
    plant_id: int,
    plant: PlantCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user_from_token),
):
    fav_plant_id = current_user.id
    plant_retrieved = retreive_plant(plant_id=plant_id, db=db)
    if not plant_retrieved:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plant with id {plant_id} does not exist",
        )
    if plant_retrieved.fav_plant_id == current_user.id or current_user.is_superuser:
        message = update_plant_by_id(
            plant_id=plant_id, plant=plant, db=db, fav_plant_id=fav_plant_id
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"You are not authorized to update.",
        )
    return {"detail": "Successfully updated data."}


@router.delete("/delete/{plant_id}")
def delete_plant(
    plant_id: int,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user_from_token),
):
    plant = retreive_plant(plant_id=plant_id, db=db)
    if not plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plant with id {plant_id} does not exist",
        )
    if plant.fav_plant_id == current_user.id or current_user.is_superuser:
        delete_plant_by_id(plant_id=plant_id, db=db, fav_plant_id=current_user.id)
        return {"detail": "Plant Successfully deleted"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted!!"
    )
