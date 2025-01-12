from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile

from settings import UserData,UserFileData
from main import chat_response_generator,chat_voice_response_generator
from agents import voice_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def root():
    return {"message": "Hello World"}

@app.post("/api/chat")
async def chat(user_data: UserData):
  return chat_response_generator(type=user_data.type, category=user_data.category, query=user_data.query, data=user_data.data)
  

@app.post("/app/chat/voice")
async def chat_voice(user_data: UserFileData ):
    return chat_voice_response_generator(type=user_data.type, category=user_data.category, file= user_data.file, data=user_data.data)

@app.post("/voice")
async def voice(file: UploadFile):
    file_bytes = await file.read()
    return voice_agent(file_bytes)