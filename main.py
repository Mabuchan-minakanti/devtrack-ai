from fastapi import FastAPI, Request
from database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "DevTrack AI connected to DB 🚀"}

