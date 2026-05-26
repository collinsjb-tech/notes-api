from fastapi import FastAPI
from pydantic import BaseModel
import uuid

add = FastAPI()
notes = []
class Notecreate(BaseModel):
    title: str
    content: str




@add.get('/')
def home():
    return {"message": "Welcome to note api"}

@add.get("/notes")
def get_notes():
    return notes


@add.get('/notes/{note_id}')
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
    return {"message": "Note not found"}

@add.post('/notes')
def create_note(note: Notecreate):
    new_note = {
        "id": str(uuid.uuid4()),
        "title": note.title,
        "content": note.content
    }
    notes.append(new_note)
    return {"message": "Note created successfully"}