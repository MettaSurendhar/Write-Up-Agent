from agents import voice_agent
from pathlib import Path
from main import chat_voice_response_generator

audio_file = Path(__file__).parent / "sample_voice02.mp3"

print("---- started testing ---")
print(voice_agent(audio_file))

data={
  "balance":"21,040"
}
response = chat_voice_response_generator("bank","account",audio_file, data)