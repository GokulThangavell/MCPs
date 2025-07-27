import pyttsx3
from agents.reasoning_agent import ReasoningAgent

class VoiceAgent(ReasoningAgent):
    def process(self, message: str) -> str:
        response = f"You said: {message}"   #Replace with real AI logic if needed

        #Speak the response using TTS
        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()

        return response