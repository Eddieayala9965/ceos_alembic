from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import session
from models import Ceos, CeosSchema, Base

app = FastAPI()


origins = [
    "http://localhost", 
    "http://localhost:5173", 

]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

@app.get('/')
def home():
    return {"message": "Root Route"}

@app.get('/ceos')
def get_ceos():
    get_url = session.query(Ceos)
    return get_url.all()


@app.post("/create/ceos")
def post_ceos( name: str, slug: str, year: int ):
    new_ceo = Ceos( name=name, slug=slug, year=year)
    session.add(new_ceo)
    session.commit()
    return {"new url": new_ceo}

def create_tables():
    Base.metadata.create_all(session)
