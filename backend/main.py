from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AskRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_agent(request: AskRequest):
    return {"answer": "This is a sample response"}
