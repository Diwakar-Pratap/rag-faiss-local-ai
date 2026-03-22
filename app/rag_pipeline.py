from app.retriever import retrieve
from app.llm import ask_llm

def run_rag(query, vector_store):
    results = retrieve(query, vector_store)

    context = ""
    sources = []

    for r in results:
        context += r["text"] + "\n"
        sources.append(r["source"])

    llm_response = ask_llm(context, query)

    # ✅ Ensure always string
    if isinstance(llm_response, dict):
        answer = llm_response.get("answer", "")
    else:
        answer = llm_response

    return {
        "answer": answer,
        "sources": sources
    }