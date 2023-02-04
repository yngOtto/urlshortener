# shortener_app/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to Otto's URL shortener API :)"