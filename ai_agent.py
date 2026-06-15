import os

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

# API Keys
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY", "")


def get_response_from_ai_agent(
    llm_id,
    query,
    allow_search,
    system_prompt,
    provider
):

    # Select Model
    if provider == "Groq":
        llm = ChatGroq(
            model=llm_id,
            temperature=0.7
        )

    elif provider == "OpenAI":
        llm = ChatOpenAI(
            model=llm_id,
            temperature=0.7
        )

    else:
        raise ValueError("Invalid Provider")

    # Tools
    tools = []

    if allow_search:
        tools.append(
            TavilySearch(max_results=3)
        )

    # Agent
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Messages
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query)
    ]

    # Invoke Agent
    response = agent.invoke(
        {
            "messages": messages
        }
    )

    # Extract Final AI Message
    return response["messages"][-1].content