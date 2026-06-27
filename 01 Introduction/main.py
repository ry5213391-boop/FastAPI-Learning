from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}

@app.get("/about")
def about():
    return {"project":"loan risk model", "version": "1.0"}