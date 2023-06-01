from db.models.plants import Plant
from db.repository.plants import create_new_plant
from db.repository.plants import retreive_plant
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
def create_plant(plant: PlantCreate, db: Session = Depends(get_db)):
    current_user = 1
    plant = create_new_plant(plant=plant, db=db, fav_plant_id=current_user)
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
