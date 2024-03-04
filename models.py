from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
from db import engine

Base = declarative_base()

class Ceos(Base):
    __tablename__ = "react-ceo"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    slug = Column(String)
    year = Column(String)
    
class CeosSchema(BaseModel):
    name: str
    slug: str
    year: str

class Config:
    populate_by_name = True

Base.metadata.create_all(engine)