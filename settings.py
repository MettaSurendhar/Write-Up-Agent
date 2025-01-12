from data import prompts
from haystack.dataclasses import ChatMessage, ChatRole
from typing import Any
from pydantic import BaseModel
from fastapi import UploadFile



## Global Variables :

# ---- App ---- #
class UserData(BaseModel):
  type: str
  category: str
  query: str
  data: dict[str, Any]

class UserFileData(BaseModel):
  type: str
  category: str
  file: UploadFile
  data: dict[str, Any]
  
# ---- Main ---- #

bank_chat_history = [
    ChatMessage(
        content="""You are 'Infinsa Intelligence,' a financial assistant. Provide insights and tips on navigating and utilizing digital banking effectively.""",
        role=ChatRole.SYSTEM,
        name="Infinsa-Agent")
]

plan_chat_history = [
    ChatMessage(
        content="""You are 'Infinsa Intelligence,' a financial assistant. Help create a strategic financial plan tailored for long-term goals and short-term needs.""",
        role=ChatRole.SYSTEM,
        name="Infinsa-Agent")
]

learn_chat_history = [
    ChatMessage(
        content="""You are 'Infinsa Intelligence,' a financial assistant. Explain key financial concepts in an easy-to-understand manner to promote financial literacy.""",
        role=ChatRole.SYSTEM,
        name="Infinsa-Intelligence")
]

## Functions 

def get_prompt_by_category(category):
    matched_prompts= list(filter(lambda p: p["category"] == category, prompts))
    return matched_prompts[0]["prompt"]

def get_chat_history_by_type(type):
  if type == "bank":
    return bank_chat_history
  elif type == "plan":
    return plan_chat_history
  elif type == "learn":
    return learn_chat_history