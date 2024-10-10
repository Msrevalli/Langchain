from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_PROJECT"]="Simple Q&A Chatbot with Ollama"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","question:{question}")
    ]
)

def generate_response(question):
    model = Ollama(model="gemma2:2b")
    outputparser=StrOutputParser()
    chain=prompt|model|outputparser
    return chain.invoke({"question":question})

st.title("Q&A Chatbot using LLama")

st.write("Write what you have in mind")

user_input=st.text_input("You:")

if user_input:
    response = generate_response(user_input)
    st.write(response)

else:
    st.write("Please provide the user input")