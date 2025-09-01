from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaLLM

app = FastAPI()

class Query(BaseModel):
    query: str

llm = OllamaLLM(model="llama2")

@app.post("/chat")
def chat(query: Query):
    response = llm(query.query)
    return {"answer": response}