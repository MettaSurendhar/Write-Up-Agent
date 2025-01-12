from typing import Any, Union
from haystack.core.component import component
from haystack.dataclasses import ChatMessage
from haystack.components.builders import PromptBuilder,ChatPromptBuilder
from haystack_integrations.components.generators.google_ai import GoogleAIGeminiGenerator,GoogleAIGeminiChatGenerator
from haystack import Pipeline
from dotenv import load_dotenv
import google.generativeai as genai
import os
import io 

os.environ["GOOGLE_API_KEY"]="google-api-key"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

@component
class Agent:

  def __init__ (self,prompt):
    self.prompt_builder = PromptBuilder(template=prompt)
    self.generator = GoogleAIGeminiGenerator(model="gemini-1.5-flash")
    self.pipeline = Pipeline()
    self.pipeline.add_component("prompt_builder", self.prompt_builder)
    self.pipeline.add_component("generator", self.generator)
    self.pipeline.connect("prompt_builder", "generator")

  @component.output_types(response=dict[str, Any])
  def run(self, query: str, data: dict[str:Any]):
    result = self.pipeline.run(
      data={
        "prompt_builder": {{"query": query}, {"data":data}}
      })
    response = result["generator"]["replies"][0]

    return response

@component
class ChatAgent:

  def __init__ (self,chat_history):
    self.chat_history = chat_history  
    self.prompt_builder = ChatPromptBuilder()
    self.generator = GoogleAIGeminiChatGenerator(model="gemini-1.5-flash")
    self.pipeline = Pipeline()
    self.pipeline.add_component("prompt_builder", self.prompt_builder)
    self.pipeline.add_component("generator", self.generator)
    self.pipeline.connect("prompt_builder", "generator")

  @component.output_types(response=dict[str, Any])
  def run(self, query: str, data: dict[str:Any], prompt: ChatMessage ):

    messages= self.chat_history + [prompt]
   
    print(" Messages : \n" , messages)
    result = self.pipeline.run(
      data={
        "prompt_builder": {
          "template_variables":{"query": query, "data":data},
          "template": messages
          }
      })
    response = result["generator"]["replies"][0].content

    return {"response":response}

def voice_agent(audio_file_bytes):
  # read file and return response
  audio_file = io.BytesIO(audio_file_bytes)
  audio_file.name = "audio.mp3"

  audio_file = genai.upload_file(audio_file, mime_type="audio/mpeg")
  prompt = "You are 'Infinsa Intelligence,' a highly knowledgeable and reliable financial assistant. Your role is to listen carefully to the user's audio queries, accurately understand their financial questions, and respond with clear, concise, and helpful answers. Always provide your responses in English, ensuring they are professional and easy to understand."
  model = genai.GenerativeModel("gemini-1.5-flash")
  result = model.generate_content([audio_file, prompt])
  return result.text