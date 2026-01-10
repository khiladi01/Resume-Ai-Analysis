from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return [{
        "name": "Raushan Raj",
        "age": 34,
        "email": "raushan505@gmail.com"
    }]

