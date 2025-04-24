from pydantic import BaseModel
from enum import Enum

class ProviderEnum(str, Enum):
    vapi = "vapi"
    retell = "retell"

class CreateAgentRequest(BaseModel):
    provider: ProviderEnum
    name: str
    description: str
    voice_id: str
    llm_id: str = None  # Only for retell