from fastapi import FastAPI, APIRouter
from src.routes.analyzer import router as analyzer_router

app = FastAPI()

app.include_router(analyzer_router)

@app.get("/")
def home():
    return {"message": "DSA AI tutor Initial Page"}

