from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.openapi.utils import get_openapi
from app.database import SessionLocal
from app import crud
from app.models import Organisation

from .inputData import *

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/organisations")
async def get_all_organisations(db: Session = Depends(get_db)):
    organisations = crud.get_all_organisations(db)
    return organisations

@app.get("/addresses")
async def get_all_addresses(db: Session = Depends(get_db)):
    addresses = crud.get_all_addresses(db)
    return addresses

@app.get("/actions")
async def get_all_actions(db: Session = Depends(get_db)):
    actions = crud.get_all_actions(db)
    return actions

@app.get("/organization_actions")
async def get_all_organization_actions(db: Session = Depends(get_db)):
    organization_actions = crud.get_all_organization_actions(db)
    return organization_actions


@app.post("/get_organisations_by_address")
async def get_organisations_by_address(building_address: str, db: Session = Depends(get_db)):
    organisations = crud.get_organisations_in_building(db, building_address)
    return organisations

@app.post("/organisations_by_action")
async def get_organisations_by_action(action_name: str, db: Session = Depends(get_db)):
    organisations = crud.get_organisations_by_action(db, action_name)
    return organisations

@app.post("/organisations_near_location")
async def get_organisations_near_location(latitude: float, longitude: float, radius_km: float, db: Session = Depends(get_db)):
    organisations = crud.get_organisations_near_location(db, latitude, longitude, radius_km)
    return organisations

@app.get("/organisation/{org_id}")
async def get_organisation_by_id(org_id: int, db: Session = Depends(get_db)):
    organisation = crud.get_organisation_by_id(db, org_id)
    return organisation

@app.post("/search_organisations_by_action_tree")
async def search_organisations_by_action_tree(action_name: str, max_depth: int = 3, db: Session = Depends(get_db)):
    organisations = crud.search_organisations_by_action_tree(db, action_name, max_depth)
    return organisations

@app.post("/search_organisation_by_name")
async def search_organisation_by_name(name: str, db: Session = Depends(get_db)):
    organisations = crud.search_organisation_by_name(db, name)
    return organisations

@app.get("/redoc", response_class=HTMLResponse)
def redoc_ui():
    return HTMLResponse("""
    <html>
        <head>
            <title>API Documentation</title>
            <script src="https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.49/bundles/redoc.standalone.js"></script>
        </head>
        <body>
            <redoc spec-url='/openapi.json'></redoc>
        </body>
    </html>
    """)

@app.get("/input")
def input():
    input3()
    return('true')