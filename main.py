from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello, Uma! FastAPI is running"}

class NameRequest(BaseModel):
    name: str

@app.post("/greet")
def greet_user(request: NameRequest):
    return {"greeting": f"Hello, {request.name}! great to meet you!"}
