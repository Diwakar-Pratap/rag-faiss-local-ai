# 🚀 Local RAG System with FAISS + Flask

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system using:
- FAISS (local vector DB)
- Sentence Transformers (embeddings)
- NVIDIA LLM API
- Flask (backend)
- HTML/JS (frontend)

## Features
- Local document ingestion (PDF, TXT)
- Chunking + batching
- FAISS similarity search
- Source tracking
- Web-based chat UI

## Setup
```bash
pip install -r requirements.txt
python main.py  # build index
python app.py   # run server