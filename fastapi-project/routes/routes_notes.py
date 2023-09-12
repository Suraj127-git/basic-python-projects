from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.config_notes import conn
from model.model_notes import Notes
from schemas.schemas_notes import NoteEntity, NotesEntity


note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def get_note(request: Request):
    docs = conn.Notes.Notes.find({})
    newdocs = []
    for doc in docs:
        newdocs.append({"id": doc["_id"], "notes": doc["notes"]})
        # print(newdocs)
        # exit()
    return templates.TemplateResponse("index.html", {"request": request, "newdocs": newdocs})

@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    formdict = dict(form)
    print(formdict)
    inserted_note = conn.Notes.Notes.insert_one(formdict)
    return {"Success": True}