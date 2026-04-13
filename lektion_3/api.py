from fastapi import FastAPI
from chat import chat
from datamodels import ChatRequest, ChatResponse



app = FastAPI()
@app.post("/chat",response_model=ChatResponse)
async def joek_chat(request: ChatRequest):
    chat_respone = await chat(request)
    return chat_respone