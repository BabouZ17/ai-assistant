import openai
import os
import streamlit as st

MODEL = "gpt-3.5-turbo"
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("💬 Jarvis")
st.caption("🚀 An ai-assistant powered by OpenAI")


if not "messages" in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Start typing"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(
        model=MODEL, messages=st.session_state.messages
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
