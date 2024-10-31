
from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Checka estooooo!"}