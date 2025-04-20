# PDF Question Answering with RAG and LangChain

This project implements a PDF-based question answering system using **Retrieval-Augmented Generation (RAG)** and **LangChain**. It loads PDF documents, extracts content, generates vector embeddings for semantic search, and uses a Large Language Model (LLM) to generate natural language answers based on retrieved context.

---

## Installation

```bash
git clone https://github.com/QuocThinh73/pdf_question_answering.git
cd pdf_question_answering
```

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn src.app:app --host 0.0.0.0 --port 5000 --reload
```

Open your browser and go to:

```
http://localhost:5000/docs
```

## Downloading PDFs

By default, `data_source/generative_ai/download.py` contains a hard‑coded `file_links` list. To add or update papers:

1. Edit `file_links` list in `download.py`.
2. Run the download script locally:
   ```bash
   python data_source/generative_ai/download.py
   ```

Downloaded PDFs will be saved in `data_source/generative_ai/`.

---

## Docker Usage

### 1. Build the Docker image

```bash
docker build -t pdf_question_answering .
```

### 2. Run the container with a volume mount

Mount `data_source` so that any PDFs you downloaded locally are visible inside the container:

```bash
docker run -d -p 5000:5000 -v "$(pwd)/data_source:/app/data_source" --name pdf_qna pdf_question_answering
```

- `-v "$(pwd)/data_source:/app/data_source"`: share your local `data_source` directory
- `-p 5000:5000`: expose FastAPI at `http://localhost:5000`


### 3. Test the API

Open your browser and go to:

```
http://localhost:5000/docs
```

Use the interactive Swagger UI to test endpoints for uploading new PDFs, querying, etc.

---