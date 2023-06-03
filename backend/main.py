# main.py
from apis.base import api_router
from core.config import settings
from db.base import Base  # import Base from db.base not db.base_clas
from db.session import engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from webapps.base import api_router as webapp_router

# from apis.general_pages.route_homepage import general_pages_router
# from db.base_class import Base


def include_router(app):
    app.include_router(api_router)  # test general_pages_router
    app.include_router(webapp_router) # webapp monolitic


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


# to create our database tables
def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESC,
        version=settings.PROJECT_VERSION,
        servers=settings.PROJECT_SERVER,
    )
    include_router(app)
    configure_static(app)
    create_tables()
    return app


# @app.get("/")
# def hello_api():
#     return {"msg":"Hello FastAPI"}

app = start_application()
