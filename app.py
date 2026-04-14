import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Bhai Ka AI", page_icon="🤖")
st.title("🤖 My Personal AI Assistant")

# Dhyan se dekho, yahan quotes (" ") lage hain
API_KEY = "AIzaSyD_y56svEeHCneSWhZDW8wRA3gUBzlcbwo"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Pucho bhai..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
