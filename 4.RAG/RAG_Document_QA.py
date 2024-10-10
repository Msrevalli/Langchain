from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import streamlit as st
import os


from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')

llm=ChatGroq(model="Gemma-7b-It")

prompt=ChatPromptTemplate.from_template(
    """
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Question:{input}

"""
)



