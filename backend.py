from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from ai_agent import get_response_from_ai_agent

import uvicorn

app = FastAPI(title="LangGraph AI Agent")


class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768",
    "gpt-4o-mini"
]


@app.post("/chat")
async def chat_endpoint(request: RequestState):

    try:

        response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=request.messages[0],
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )

        return {
            "status": "success",
            "response": response
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/")
async def root():
    return {
        "message": "AI Agent Backend Running Successfully"
    }


if __name__ == "__main__":
    uvicorn.run(
        "backend:app",
        host="127.0.0.1",
        port=9999,
        reload=True
    )