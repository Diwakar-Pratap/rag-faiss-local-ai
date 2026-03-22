# 🤖 Local RAG Chatbot with FAISS + Flask

A **Retrieval-Augmented Generation (RAG)** based AI chatbot that answers questions using your **local documents (PDF/TXT)** by combining:

* Local embeddings
* FAISS vector database
* Flask backend
* Web-based chat UI
* NVIDIA LLM API

---

## 🚀 Features

* 📂 **Multi-document ingestion** (PDF + TXT from your system)
* 🧠 **Semantic search using embeddings**
* ⚡ **FAISS local vector database (fast + offline)**
* 🌐 **Flask backend with chat API**
* 💬 **Web-based chat UI**
* 📌 **Source tracking (shows file paths)**
* 🔁 **Scalable RAG pipeline with batching**
* 🆓 **Local embeddings (Sentence Transformers)**

---

## 🏗️ Architecture

```
Local Files (PDF/TXT)
        ↓
Text Chunking
        ↓
Embeddings (MiniLM)
        ↓
FAISS Vector DB (Local)
        ↓
User Query
        ↓
Similarity Search
        ↓
Context Retrieval
        ↓
NVIDIA LLM Response
```

---

## 📁 Project Structure

```
rag-faiss/
│
├── app/
│   ├── config.py
│   ├── embeddings.py        # Embedding model
│   ├── vector_store.py      # FAISS logic + metadata
│   ├── retriever.py         # Search logic
│   ├── llm.py               # NVIDIA LLM API
│   ├── rag_pipeline.py      # Full RAG pipeline
│   ├── chunking.py          # Text chunking
│   └── data_loader.py       # Load PDF/TXT files
│
├── templates/
│   └── index.html           # Chat UI (Flask)
│
├── faiss_index/             # Stored vector DB (ignored in git)
│
├── app.py                   # Flask backend
├── main.py                  # Index builder
├── .env                     # API keys
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-faiss-local-ai.git
cd rag-faiss-local-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```
NVIDIA_API_KEY=your_nvidia_api_key
```

---

### 5️⃣ Build FAISS Index

```bash
python main.py
```

* Choose option: `1`
* Enter folder path (e.g. `C:\Users\Diwakar\Documents`)

This will:

* Load documents
* Chunk text
* Generate embeddings
* Store vectors in FAISS

---

### 6️⃣ Run Backend Server

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 💬 API Usage

### POST `/chat`

#### Request

```json
{
  "query": "What is FAISS?"
}
```

#### Response

```json
{
  "answer": "FAISS is a library for efficient similarity search...",
  "sources": [
    "C:\\Users\\Diwakar\\Documents\\file1.txt",
    "C:\\Users\\Diwakar\\Notes\\doc.pdf"
  ]
}
```

---

## 🧠 Technologies Used

* Python 3.x
* Flask
* FAISS (Vector Database)
* Sentence Transformers
* NVIDIA LLM API
* NumPy
* HTML + JavaScript

---

## 🔥 Key Features Implemented

* ✅ Local vector database (FAISS)
* ✅ File ingestion (PDF + TXT)
* ✅ Chunking + batching for scalability
* ✅ Metadata tracking (source files)
* ✅ REST API with Flask
* ✅ Interactive web UI
* ✅ Large data handling (10K+ chunks)

---

## 🔮 Future Improvements

* 📌 Source highlighting (exact paragraph)
* 💬 Chat history (multi-turn memory)
* ⚡ Streaming responses (real-time typing)
* 📤 File upload UI
* 🔍 Hybrid search (BM25 + vector)
* 🐳 Docker deployment
* ☁️ Cloud deployment (AWS/GCP)

---

## 📌 Key Learnings

* RAG pipeline architecture
* Vector similarity search with FAISS
* Embedding generation using transformers
* Building scalable indexing pipelines
* Backend API development with Flask
* Handling large-scale document ingestion

---

## 🤝 Contributing

Feel free to fork this repository and enhance the system.

---

## 📄 License

This project is open-source and available under the MIT License.
