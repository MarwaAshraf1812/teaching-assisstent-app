# Teaching Assistant App

A Retrieval-Augmented Generation (RAG) teaching assistant that helps people understand their study materials. Upload a PDF, ask questions about it in plain language, and get answers based on the document, with page references to help you verify the information.

## What It Does

- Accepts PDF documents uploaded by a user.
- Extracts and indexes the document's text so it can be searched by meaning.
- Answers questions using relevant passages from the uploaded PDF.
- Includes source references, such as page numbers, with answers where available.
- Keeps the conversation focused on the selected document rather than relying only on general model knowledge.

## How It Works

1. The user uploads a PDF.
2. The backend extracts its text and splits it into smaller passages.
3. The passages are converted into embeddings and stored in a vector database.
4. When the user asks a question, the system retrieves relevant passages.
5. The language model uses those passages to produce an answer with document references.

## Planned Technology

- **Python** for the backend
- **FastAPI** for the API and document-related endpoints
- **RAG pipeline** for retrieval-grounded answers
- **PDF text extraction**, an **embedding model**, a **vector database**, and an **LLM provider** to be selected during implementation

The specific model provider and vector database have not been selected yet.

## Project Status

This repository is at the initial setup stage. The application, API routes, dependency list, and run instructions are not implemented yet.

## Local Development

Python 3.10 or newer is recommended. Create and activate a virtual environment from the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install and run instructions will be added once the backend dependencies and application entry point are in place.

## Planned Improvements

- Support multiple PDFs and document collections.
- Show citations that link answers to the relevant PDF pages.
- Handle scanned PDFs with OCR where needed.
- Add document and conversation management.
- Add upload validation, file-size limits, and clear document-retention controls.
