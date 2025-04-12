from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uuid import uuid4 
from google.cloud import firestore
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi import Query, Body

app = FastAPI()
firestore_db = firestore.Client()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Landing page route
@app.get("/", response_class=HTMLResponse)
def get_landingpage(request: Request):
    return templates.TemplateResponse("landingpage.html", {"request": request})


