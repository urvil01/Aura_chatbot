# Aura_chatbot

Aura Chatbot Agent is a Python-based chatbot application that utilizes FastAPI, Streamlit, LangGraph, LangChain, Groq, OpenAI, and Tavily Search.

This app helps users build custom AI agents with unique system prompts, model choices, and web search capabilities.

✨ Features
Creating Custom AI Agents
Groq and OpenAI Models Integration
Real-time Web Search Capabilities using Tavily
FastAPI Server
Streamlit Client UI
LangGraph Agent System
Dynamic Prompting
Interactive UI
Cloud-Deployable Application
🛠️ Technologies Used
Frontend Technologies
Streamlit
Backend Technologies
FastAPI
Uvicorn Server
Agent AI & Development Tools
LangGraph
LangChain
Models Used
Groq (Llama 3.3 70B)
OpenAI GPT Models
Web Search Engine
Tavily Search API
📂 Project Directory
Aura_Chatbot/
│
├── ai_agent.py   # agent logic implementation
├── backend.py    # FastAPI backend development
├── frontend.py   # Streamlit front-end UI design
├── requirements.txt
├── .gitignore
└── README.md
🚀 How It Works
The user inputs their own system prompt.
The user chooses an AI provider model.
The user enters the query.
FastAPI forwards the request to the AI Agent.
LangGraph runs the agent process flow.
Optional Tavily search fetches live data.
The response is generated and shown in Streamlit.
⚙️ Installation
Clone Repo
git clone https://github.com/your-username/aura-chatbot.git
cd aura-chatbot
Create Virtual Env
python -m venv venv
Activate Virtual Env

For Windows:

venv\Scripts\activate

For Mac/Linux:

source venv/bin/activate
Install Deps
pip install -r requirements.txt
🔑 Environment Vars

Create a .env file in the root folder:

GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
▶️ Backend Execution
python backend.py

Backend URL:

http://127.0.0.1:9999
▶️ Frontend Execution
streamlit run frontend.py
Users can:

Create customized AI avatars 
Pose questions 
Activate web searches 
Toggle AI model selection 
Get instant intelligent replies
🎯 Features for the Future
Chat History and Recall 
Multi-Agents Processes 
User Authentication 
Speech Input/Output Support 
File Upload 
Conversation Export 
Vector Database Connection
👨‍💻 Author

Urvil Dudakiya

Passionate Python Developer and Artificial Intelligence Engineer who aims to create AI-enabled applications utilizing latest LLM technologies.

If you liked this project please ⭐ it on GitHub.
