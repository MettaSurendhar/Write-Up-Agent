from typing import Any

from agents import Agent,ChatAgent, voice_agent
from haystack.dataclasses import ChatMessage
from settings import bank_chat_history, get_prompt_by_category,get_chat_history_by_type

# /chat/{type}?category=
# type = account/plan/learn

# /generate/?category=
# recommendations_budget/financial_health

## --- Chat Response Generator --- ##
def chat_response_generator(type: str, category: str, query: str, data: dict[str, Any]):
  
  chat_history = get_chat_history_by_type(type)
  chat_agent = ChatAgent(chat_history)
  prompt = get_prompt_by_category(category=category)
  user_prompt=ChatMessage.from_user(prompt)

  result = chat_agent.run(query,data,user_prompt)
  response = result["response"]

  chat_history.append(ChatMessage.from_user(query))
  chat_history.append(ChatMessage.from_assistant(response))

  return response

## --- Chat Voice Response Generator --- ##
def chat_voice_response_generator(type: str, category: str, file, data: dict[str, Any]):
  
  chat_history = get_chat_history_by_type(type)
  chat_agent = ChatAgent(chat_history)
  prompt = get_prompt_by_category(category=category)
  user_prompt=ChatMessage.from_user(prompt)
  query = voice_agent(file)
  result = chat_agent.run(query,data,user_prompt)
  response = result["response"]

  chat_history.append(ChatMessage.from_user(query))
  chat_history.append(ChatMessage.from_assistant(response))

  return response

  ## --- Response Generator --- ##

def response_generator(category: str, query: str, data: dict[str, Any]):

  prompt = get_prompt_by_category(category=category)
  agent = Agent(prompt)

  result = agent.run(query,data)
  response = result["response"]

  return response


## Example use : 
data={
  "balance":"21,040"
}
# response = chat_response_generator("bank","account","how can i use my account balance usefully ?", data)
# response = response_generator("recommendations_budget","how can i use my account balance usefully ?", data)
# print(response)


