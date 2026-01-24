from fastapi import FastAPI
from backend.config.setting import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)

@app.get("/")
async def root():
    return {"message": "Welcome to the Resume AI Analysis API"}

# Add more routes here as needed
