# Unified Agent API

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## .env variables

- VAPI_API_KEY
- RETELL_API_KEY

## Sample Request

```json
{
  "provider": "vapi",
  "name": "Agent Smith",
  "description": "Helpful assistant",
  "voice_id": "en-US-1",
  "llm_id": "gpt-3.5-turbo"  # required only for retell
}
```

