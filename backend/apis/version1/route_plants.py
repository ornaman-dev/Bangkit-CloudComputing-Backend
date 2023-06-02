# apis > version1 > route_plants.py
from typing import List  # for list view

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.plants import create_new_plant
from db.repository.plants import delete_plant_by_id  # for delete plant by id
from db.repository.plants import list_plants  # for list view
from db.repository.plants import retreive_plant
from db.repository.plants import update_plant_by_id  # for update plant by id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.plants import PlantCreate
from schemas.plants import ShowPlant
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/create-plant/", response_model=ShowPlant)
# def create_plant(plant: PlantCreate, db: Session = Depends(get_db)):
#     current_user = 1
#     plant = create_new_plant(plant=plant, db=db, fav_plant_id=current_user)
#     return plant
def create_plant(
    plant: PlantCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    plant = create_new_plant(plant=plant, db=db, fav_plant_id=current_user.id)
    return plant


# function retreive plant dari database
@router.get(
    "/get/{plant_id}", response_model=ShowPlant
)  # if we keep just "{id}" . it would stat catching all routes
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


@router.put("/update/{plant_id}")  # new
def update_plant(plant_id: int, plant: PlantCreate, db: Session = Depends(get_db)):
    current_user = 1
    message = update_plant_by_id(
        plant_id=plant_id, plant=plant, db=db, fav_plant_id=current_user
    )
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plant with plant_id {plant_id} not found",
        )
    return {"msg": "Successfully updated data."}


@router.delete("/delete/{plant_id}")
def delete_plant(
    plant_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    plant = retreive_plant(plant_id=plant_id, db=db)
    if not plant:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Plant with {plant_id} does not exist",
        )
    print(plant.fav_plant_id, current_user.id, current_user.is_superuser)
    if plant.fav_plant_id == current_user.id or current_user.is_superuser:
        delete_plant_by_id(plant_id=plant_id, db=db, fav_plant_id=current_user.id)
        return {"msg": "Successfully deleted."}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not permitted!!!!"
    )
