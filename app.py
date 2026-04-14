import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Bhai Ka AI", page_icon="🤖")
st.title("🤖 My Personal AI Assistant")

# Tumhari API Key
genai.configure(api_key="AIzaSyDCO-9_tNJOPznZ8q3-w67ctblP4btFIXs")
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
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
