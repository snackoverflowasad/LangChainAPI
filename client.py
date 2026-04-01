import streamlit as st
import requests
st.title("LangChain API demo")
input_text = st.text_input("Write an poem...")

def get_res(txt):
    res = requests.post("http://localhost:8800/llm/res/openai/invoke",
                        json={
                            'input' : {
                                'topic' : input_text
                            }
                        })
    return res.json()['output']['content']


if input_text:
    st.write(get_res(input_text))