# streamlit_app.py

import streamlit as st
import requests
import json

# API endpoint
url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json'
}

# Session state to persist history between interactions
if "history" not in st.session_state:
    st.session_state.history = []

st.title("CodeMonarch Chat - SubhamIO")

prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Generate Response"):
    if prompt:
        # Update history
        st.session_state.history.append(prompt)
        final_prompt = "\n".join(st.session_state.history)

        data = {
            "model": "CodeMonarch",
            "prompt": final_prompt,
            "stream": False
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            data = json.loads(response.text)
            actual_response = data.get("response", "")
            st.text_area("Response:", actual_response, height=200)
        else:
            st.error(f"Error: {response.status_code}\n{response.text}")
    else:
        st.warning("Please enter a prompt to continue.")
