from sqlalchemy import create_engine
from database import Base

engine = create_engine("sqlite:///./test.db")

Base.metadata.drop_all(bind=engine, tables=[Base.metadata.tables['user']])
