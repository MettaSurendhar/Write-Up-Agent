from typing import Any

from agents import Agent,ChatAgent
from haystack.dataclasses import ChatMessage, ChatRole
from chat_history import get_linkedin_chat_history, get_twitter_chat_history, update_linkedin_chat_history
from prompt import get_prompt, writing_style_prompt
from config import agent_settings


## --- Chat Response Generator --- ##
def chat_response_generator(media_type: str, category_type: str, data: str):

  chat_history=None
  agent_chat_history=None
  prompt=None
  if media_type == "linkedin":
    chat_history = get_linkedin_chat_history(category_type)
    agent_chat_history = [ChatMessage(content= agent_settings['agent_description'][media_type], role=ChatRole.SYSTEM,name=agent_settings['agent_name'])]
  elif media_type == "twitter":
    chat_history = get_twitter_chat_history(category_type)
    agent_chat_history = [ChatMessage(content= agent_settings['agent_description'][media_type], role=ChatRole.SYSTEM,name=agent_settings['agent_name'])]
    
  prompt = get_prompt(media_type,category_type)
  history = agent_chat_history + chat_history
  user_prompt= ChatMessage(content=prompt, role=ChatRole.USER, name="Metta")
  chat_agent = ChatAgent(history)
  result = chat_agent.run(data,user_prompt)

  response = result["response"]
  return response

# --- Response Generator --- ##
def response_generator(data: str):
  writing_style_agent = Agent(writing_style_prompt)
  response = writing_style_agent.run(data)
  return response

## Example usage chat response generator: 
# info=" Blog Information: /n Blog Title: From Newbie to Web Developer /n Blog: Starting out in web development can feel a bit like navigating a maze with no map. In my latest blog post, I share how I went from a complete newbie to building my own websites. I talk about the struggles I faced, the resources that helped me, and some tips that might make your path a bit smoother. /n Blog Link: Metta’s Tech Bytes 🚀." 
# writing_style="Preferred Writing Style: /n no emoji,more professional"
# data = info+"/n/n"+writing_style
# data = info
# response = chat_response_generator("blog", data )
# update_linkedin_chat_history("blog",data,response)
# print(response)


## Example usage response generator
# data="no emoji /n professional /n friendly /n engaging"
# print(response_generator(data))