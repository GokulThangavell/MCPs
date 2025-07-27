import requests
import os
from .base_agent import BaseAgent

class ReasoningAgent(BaseAgent):
    def handle_message(self, message:str) -> str:
        ollama_url = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
        model_name = os.getenv("OLLAMA_MODEL_NAME", "mistral")

        response = requests.post(
            f"{ollama_url}/api/generate",
            json = {"model": model_name, "prompt":message, "stream": False}
        )
        return response.json()
        ##try:
          ##  data = response.json()
        ##except requests.exceptions.JSONDecodeError:
            ##print("Ollama returned non-JSON content")
            ##print(response.text)
            ##data = {"response":response.text}
        ##print ("Raw response from Ollama:")
        ##return response.text