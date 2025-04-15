from src.rag.main import build_rag_chain, InputQA, OutputQA
from src.base.llm_model import get_hf_llm
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"


# -- Initialize LLM and Chain --
llm = get_hf_llm(temperature=0.9)
genai_docs = "./data_source/generative_ai"

# Build RAG chain
genai_chain = build_rag_chain(llm, data_dir=genai_docs, data_type="pdf")

# -- FastAPI App --
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain’s Runnable interfaces",
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# -- Routes --


@app.get("/check")
async def check():
    return {"status": "ok"}


@app.post("/generative_ai", response_model=OutputQA)
async def generative_ai(inputs: InputQA):
    answer = genai_chain.invoke(inputs.question)
    return {"answer": answer}

# -- LangServe Playground Route --
add_routes(
    app,
    genai_chain,
    playground_type="default",
    path="/generative_ai"
)
