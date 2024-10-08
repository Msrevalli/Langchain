from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

model = ChatGroq(model="Gemma2-9b-It")

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate([
    ('system',system_template),
    ('user','{text}')
])

parser = StrOutputParser()

chain = prompt_template|model|parser

app=FastAPI(title="Langchain server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces")

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)