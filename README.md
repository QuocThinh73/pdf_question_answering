# PDF Question Answering with RAG and LangChain

This project implements a PDF-based question answering system using **Retrieval-Augmented Generation (RAG)** and **LangChain**. It loads PDF documents, extracts content, generates vector embeddings for semantic search, and uses a Large Language Model (LLM) to generate natural language answers based on retrieved context.


## Installation

```bash
git clone https://github.com/QuocThinh73/pdf_question_answering.git
cd pdf_question_answering
pip install -r requirements.txt
```

## Running the App

Start the server with:

```bash
uvicorn src.app:app --host "0.0.0.0" --port 5000 --reload
```

Then open your browser at http://localhost:5000/docs to access the Swagger UI for testing the API.