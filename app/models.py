from sqlalchemy import Column, Integer, String, ForeignKey, Text, Index ,ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OrganizationActions(Base):
    __tablename__ = "organizationactions"

    id = Column(Integer, primary_key=True, index=True)
    organisation_id = Column(Integer, ForeignKey("organisations.id"))
    action_id = Column(Integer, ForeignKey("actions.id"))

    __table_args__ = (
        ForeignKeyConstraint(['organisation_id'], ['organisations.id']),
        ForeignKeyConstraint(['action_id'], ['actions.id']),
    )

class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255), unique=True, index=True)
    coordinates = Column(Text)

    organisations = relationship("Organisation", back_populates="address")

    __table_args__ = (
        Index('ix_address_coordinates', 'coordinates'),
    )

class Organisation(Base):
    __tablename__ = "organisations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    telephone_number = Column(String(15), unique=True, index=True)

    address_id = Column(Integer, ForeignKey("addresses.id"))
    address = relationship("Address", back_populates="organisations")

    actions = relationship("Action", secondary="organizationactions", back_populates="organisations")

    __table_args__ = (
        Index('ix_organisation_name_telephone', 'name', 'telephone_number'),
    )

class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

    parent_id = Column(Integer, ForeignKey("actions.id"), nullable=True)
    children = relationship("Action", backref="parent", remote_side=[id])

    organisations = relationship("Organisation", secondary="organizationactions", back_populates="actions")

    __table_args__ = (
        Index('ix_action_name_parent', 'name', 'parent_id'),
    )
