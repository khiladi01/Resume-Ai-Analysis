app = FastAPI()

@app.get("/")
def home():
    return [{
        "name": "Raushan Raj",
        "age": 34,
        "email": "raushan505@gmail.com"
    }]
=======
from fastapi import FastAPI
from routes.resume_routes import router as resume_router

app = FastAPI()

app.include_router(resume_router, prefix="/api/resume", tags=["resume"])

@app.get("/")
def home():
    return [{
        "name": "Raushan Raj",
        "age": 34,
        "email": "raushan505@gmail.com"
    }]
