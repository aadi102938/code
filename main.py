from fastapi import FastAPI, HTTPException
from schemas import CreateAgentRequest

app = FastAPI()

import os
import httpx
from schemas import CreateAgentRequest

async def create_vapi_agent(data: CreateAgentRequest):
    url = "https://docs.vapi.ai/api-reference/assistants/create"
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": data.name,
        "description": data.description,
        "voice": data.voice_id,
        "tools": [],
        "model": "gpt-3.5-turbo"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        return response.json()

async def create_retell_agent(data: CreateAgentRequest):
    url = "https://docs.retellai.com/api-references/create-agent"
    headers = {
        "Authorization": f"Bearer {os.getenv('RETELL_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "voice_id": data.voice_id,
        "llm_response_engine": {
            "llm_model_id": data.llm_id
        }
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        return response.json()



@app.post("/create-agent")
async def create_agent(agent_data: CreateAgentRequest):
    if agent_data.provider == "vapi":
        return await create_vapi_agent(agent_data)
    elif agent_data.provider == "retell":
        return await create_retell_agent(agent_data)
    else:
        raise HTTPException(status_code=400, detail="Invalid provider")