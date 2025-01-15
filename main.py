from typing import Any

from agents import Agent,ChatAgent
from haystack.dataclasses import ChatMessage, ChatRole
from chat_history import get_linkedin_chat_history, update_linkedin_chat_history
from prompt import get_linkedin_prompt, writing_style_prompt
from config import agent_settings


## --- Chat Response Generator --- ##
def chat_response_generator(type: str, data: str):
  print("chat data:/n"+data)
  linkedin_chat_history = get_linkedin_chat_history(type)
  agent_chat_history = [ChatMessage(content=agent_settings['agent_description']['linkedin'],role=ChatRole.SYSTEM,name=agent_settings['agent_name'])] 
  chat_history = agent_chat_history + linkedin_chat_history

  prompt = get_linkedin_prompt(type)
  user_prompt=ChatMessage(content=prompt, role=ChatRole.USER, name="Metta")
  
  chat_agent = ChatAgent(chat_history)

  result = chat_agent.run(data,user_prompt)
  response = result["response"]
  print("chat_response:/n"+response)
  return response


## --- Chat Voice Response Generator --- ##
# def chat_voice_response_generator(type: str, category: str, file, data: dict[str, Any]):
  
#   chat_history = get_chat_history_by_type(type)
#   chat_agent = ChatAgent(chat_history)
#   prompt = get_prompt_by_category(category=category)
#   user_prompt=ChatMessage.from_user(prompt)
#   query = voice_agent(file)
#   result = chat_agent.run(query,data,user_prompt)
#   response = result["response"]

#   chat_history.append(ChatMessage.from_user(query))
#   chat_history.append(ChatMessage.from_assistant(response))

#   return response


# --- Response Generator --- ##
def response_generator(data: str):
  print("writing data"+data)
  writing_style_agent = Agent(writing_style_prompt)
  response = writing_style_agent.run(data)
  print("response:/n"+response)
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