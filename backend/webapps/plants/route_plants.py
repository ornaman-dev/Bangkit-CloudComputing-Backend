# webapps > plants > route_plants.py
from apis.version1.route_login import get_current_user_from_token
from db.models.users import Users
from db.repository.plants import create_new_plant
from db.repository.plants import list_plants
from db.repository.plants import retreive_plant
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import responses
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.templating import Jinja2Templates
from schemas.plants import PlantCreate
from sqlalchemy.orm import Session
from webapps.plants.forms import PlantCreateForm

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    plants = list_plants(db=db)
    return templates.TemplateResponse(
        "plants/homepage.html", {"request": request, "plants": plants, "msg": msg}
    )


@router.get("/detail/{plant_id}")
def plant_detail(plant_id: int, request: Request, db: Session = Depends(get_db)):
    plant = retreive_plant(plant_id=plant_id, db=db)
    return templates.TemplateResponse(
        "plants/detail.html", {"request": request, "plant": plant}
    )


@router.get("/post-a-plant/")
def create_plant(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("plants/create_plant.html", {"request": request})


@router.post("/post-a-plant/")
async def create_plant(request: Request, db: Session = Depends(get_db)):
    form = PlantCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: Users = get_current_user_from_token(token=param, db=db)
            plant = PlantCreate(**form.__dict__)
            plant = create_new_plant(plant=plant, db=db, fav_plant_id=current_user.id)
            return responses.RedirectResponse(
                f"/detail/{plant.plant_id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("plants/create_plant.html", form.__dict__)
    return templates.TemplateResponse("plants/create_plant.html", form.__dict__)


@router.get("/delete-plant/")
def show_plants_to_delete(request: Request, db: Session = Depends(get_db)):
    plants = list_plants(db=db)
    return templates.TemplateResponse(
        "plants/show_plants_to_delete.html", {"request": request, "plants": plants}
    )
