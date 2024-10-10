import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]='true'

os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot With OPENAI"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question):
    
    model=ChatOpenAI(max_tokens=1000)
    output_parser = StrOutputParser()
    chain = prompt|model|output_parser
    answer=chain.invoke({"question":question})
    return answer

st.title("Enhanced Q&A Chatbot with OpenAI")
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input)
    st.write(response)
else:
    st.write("Please provide query")





