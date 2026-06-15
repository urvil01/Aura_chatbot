# 🤖 Aura Chatbot Agent

Aura Chatbot Agent is an AI-powered chatbot application built with **Python, FastAPI, Streamlit, LangGraph, LangChain, Groq, OpenAI, and Tavily Search**.

The platform allows users to create custom AI agents by defining system prompts, selecting AI models, and enabling real-time web search capabilities.

---

## ✨ Features

* 🎯 Custom AI Agent Creation
* 🤖 Groq & OpenAI Model Integration
* 🌐 Real-Time Web Search with Tavily
* ⚡ FastAPI Backend
* 🎨 Interactive Streamlit User Interface
* 🔄 LangGraph Agent Workflow
* 📝 Dynamic System Prompt Support
* ☁️ Cloud Deployment Ready
* 🚀 Fast and Scalable Architecture

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI & Agent Framework

* LangGraph
* LangChain

### Models

* Groq (Llama 3.3 70B Versatile)
* OpenAI GPT Models

### Search Tool

* Tavily Search API

---

## 📂 Project Structure

```bash
Aura_Chatbot/
│
├── ai_agent.py        # AI Agent Logic
├── backend.py         # FastAPI Backend
├── frontend.py        # Streamlit Frontend
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 How It Works

1. User enters a custom system prompt.
2. User selects an AI provider and model.
3. User submits a query.
4. FastAPI sends the request to the AI Agent.
5. LangGraph executes the agent workflow.
6. Tavily Search retrieves live information (optional).
7. The generated response is displayed in the Streamlit UI.

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/urvil01/aura_chatbot.git
cd aura_chatbot
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Backend

```bash
python backend.py
```

Backend URL:

```text
http://127.0.0.1:9999
```

---

## ▶️ Run the Frontend

```bash
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 🌐 Deployment

### Backend Deployment

* Render

### Frontend Deployment

* Streamlit Community Cloud

---

## 📸 Application Capabilities

Users can:

* Create custom AI personas
* Ask questions using natural language
* Enable real-time web search
* Switch between Groq and OpenAI models
* Receive intelligent AI-generated responses
* Customize chatbot behavior using system prompts

---

## 🎯 Future Enhancements

* Chat Memory & Conversation History
* Multi-Agent Workflows
* User Authentication System
* Voice Input & Output
* File Upload & Analysis
* Conversation Export
* Vector Database Integration
* RAG (Retrieval-Augmented Generation)

---

## 👨‍💻 Author

### Urvil Dudakiya

Aspiring Python Developer and AI Engineer passionate about building AI-powered applications using modern Large Language Models (LLMs), Agentic AI, and Generative AI technologies.

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub. Your support is appreciated!

---

### Built with ❤️ using Python, FastAPI, Streamlit, LangGraph, LangChain, Groq, and OpenAI.
