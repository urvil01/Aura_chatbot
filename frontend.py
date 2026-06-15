import streamlit as st
import requests

st.set_page_config(page_title="Aura Agent", layout="centered")
st.title("Aura AI chatbot agent")
st.write("Create and Interect with the AI Agent!")

system_prompt = st.text_area("Define your AI Agent",height = 70,placeholder="Type Your prompt here...")

MODEL_NAMES_GROQ=["llama-3.3-70b-versatile","mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("select Provider:",("Groq","OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:",MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model=st.selectbox("Select OpenAI Model:",MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Define your AI Agent",height = 70,placeholder="Ask Anything!")

API_URL="http://127.0.0.1:9999/chat"
if st.button("Ask Agent!"):
    if user_query.strip():
        payload = {
                  "model_name": selected_model,
                  "model_provider": provider,
                  "system_prompt": system_prompt,
                  "messages": [user_query],
                  "allow_search": allow_web_search
                  }
        
        try:
              response = requests.post(API_URL, json=payload, timeout=30)
          
              st.write("Status Code:", response.status_code)
          
              if response.status_code == 200:
                 response_data = response.json()

                 st.subheader("Agent Response")

              if response_data.get("status") == "success":
                  st.markdown(response_data["response"])
              else:
                  st.error("Failed to get response")
          

          
        except Exception as e:
              st.error(f"Request failed: {e}")

        
