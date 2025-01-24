from pydantic import BaseModel
from typing import List, Optional

class AddressCreate(BaseModel):
    address: str
    coordinates: str

    class Config:
        orm_mode = True

class Address(BaseModel):
    id: int
    address: str
    coordinates: str

    class Config:
        orm_mode = True


class ActionCreate(BaseModel):
    name: str
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True

class Action(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None
    children: List["Action"] = []

    class Config:
        orm_mode = True

class OrganisationCreate(BaseModel):
    name: str
    telephone_number: str
    address_id: int
    action_id: int

    class Config:
        orm_mode = True

class Organisation(BaseModel):
    id: int
    name: str
    telephone_number: str
    address_id: int
    action_id: int

    address: Address
    action: Action 

    class Config:
        orm_mode = True


class BuildingAddressRequest(BaseModel):
    building_address: str