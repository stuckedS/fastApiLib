from sqlalchemy.orm import Session
from app.models import Organisation, Address, OrganizationActions, Action

def get_organisations_in_building(db: Session, building_address: str):
    return db.query(Organisation).join(Address).filter(Address.address == building_address).all()

def get_organisations_by_action(db: Session, action_name: str):
    action_ids = db.query(Action.id).filter(Action.name.like(f"%{action_name}%")).all()
    action_ids = [action_id[0] for action_id in action_ids]
    return db.query(Organisation).join(OrganizationActions).filter(OrganizationActions.action_id.in_(action_ids)).all()

def get_organisations_near_location(db: Session, latitude: float, longitude: float, radius_km: float):
    organisations = db.query(Organisation, Address).join(Address).all()
    nearby_organisations = []
    for org, address in organisations:
        org_lat, org_lon = map(float, address.coordinates.split(","))
        distance = ((latitude - org_lat) ** 2 + (longitude - org_lon) ** 2) ** 0.5
        if distance <= radius_km:
            nearby_organisations.append(org)
    return nearby_organisations

def get_organisation_by_id(db: Session, org_id: int):
    return db.query(Organisation).filter(Organisation.id == org_id).first()

def search_organisations_by_action_tree(db: Session, action_name: str, max_depth=3):
    root_action = db.query(Action).filter(Action.name == action_name).first()
    if not root_action:
        return []
    
    def get_descendants(action, depth):
        if depth > max_depth:
            return []
        descendants = []
        children = db.query(Action).filter(Action.parent_id == action.id).all()
        for child in children:
            descendants.append(child)
            descendants.extend(get_descendants(child, depth + 1))
        return descendants

    descendants = get_descendants(root_action, 1)
    action_ids = [action.id for action in descendants]
    return db.query(Organisation).join(OrganizationActions).filter(OrganizationActions.action_id.in_(action_ids)).all()

def search_organisation_by_name(db: Session, name: str):
    return db.query(Organisation).filter(Organisation.name.ilike(f"%{name}%")).all()

def get_all_organisations(db: Session):
    return db.query(Organisation).all()

def get_all_addresses(db: Session):
    return db.query(Address).all()

def get_all_actions(db: Session):
    return db.query(Action).all()

def get_all_organization_actions(db: Session):
    return db.query(OrganizationActions).all()