from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
app = FastAPI(
    title="LangChain Server",
    version="1.0.0",
    description="A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/llm/openai"
)

model=ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = ChatPromptTemplate.from_template("Write me an poem about {topic} in 2 paragraphs")

add_routes(
    app,
    prompt | model,
    path="/llm/res/openai"
)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8800
    )