from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from openai import OpenAI
from typing import List
# import asyncio

client = OpenAI(
    api_key="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",
)

#
class Role(BaseModel):
    role:str
    content:str
#

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_chat_completion(messages, model="gpt-3.5-turbo"):
  
   # Calling the ChatCompletion API
   newMessages = []
   for item in messages:
       newMessages.append({
           "role": item.role,
           "content": item.content
       }) 
   response = client.chat.completions.create(
       model=model,
       messages=newMessages,
       temperature=0,
       max_tokens=1000
   )

   # Returning the extracted response
   return response.choices[0].message.content


@app.post("/chat-gpt")
async def chat(messages: List[Role]):
    return get_chat_completion(messages)
