from fastapi import FastAPI
from .routers import auth, notes
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Notes API",
    description="A secure notes API with authentication",
    version="2.0.0"
)

app.include_router(auth.router)
app.include_router(notes.router)

@app.get("/")
def home():
    return {"message": "Welcome to Notes API v2"}