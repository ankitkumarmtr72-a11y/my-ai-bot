import os
# Ye line naye version ko install karne ke liye hai
os.system('pip install --upgrade google-generativeai')

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Bhai Ka AI", page_icon="🤖")
st.title("🤖 My Personal AI Assistant")

# TERI ASLI API KEY (Screenshot 005702.png se check ki maine)
API_KEY = "AIzaSyD_y56svEeHCneSWhZDW8wRA3gUBzlcbow"
genai.configure(api_key=API_KEY)

# Stable Model
model = genai.GenerativeModel('gemini-1.5-flash')

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
