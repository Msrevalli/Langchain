import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv('LANGCHAIN_PROJECT')

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain Demo with Gemma")
input_text = st.text_input("What question you have in mind?")

llm = Ollama(model="llama3.1cl")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
