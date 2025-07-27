from fastapi import FastAPI, Request
from agents.reasoning_agent import ReasoningAgent
from agents.voice_agent import VoiceAgent

app = FastAPI()

@app.post("/mcp")
async def handle_message(request:Request):
    data = await request.json()
    agent_type = data.get("agent", "reasoning")
    message = data.get("message", "")

    if(agent_type == "voice"):
        agent = VoiceAgent()
    else:
        agent = ReasoningAgent()

    response = agent.handle_message(message)
    return {"response":response}