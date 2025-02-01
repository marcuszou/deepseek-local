# _*_ coding: utf-8 _*_

# Load packages
import ollama
import streamlit as st

## Set the model
desiredModel='deepseek-r1:7b'

## Web App starts here
st.title("Run DeepSeek-R1 LLM locally")

def generate_response(questionToAsk):
    response = ollama.chat(model=desiredModel, messages=[
        {
            'role': 'user',
            'content': questionToAsk,
        },
    ])
    st.info(response['message']['content'])

with st.form("llm_form"):
    text = st.text_area(
        "Enter text:",
        "Ask a question here and press the Submit button.",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)