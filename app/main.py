from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import load_qa_chain

app = FastAPI(title="AI Assistant")

qa_chain = load_qa_chain()

class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "AI assistant API is running"}


@app.post("/ask")
def ask_question(request: QueryRequest):
    response = qa_chain.invoke(request.question)
    return {"answer": response}