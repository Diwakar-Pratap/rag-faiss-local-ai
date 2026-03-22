from flask import Flask, render_template, request, jsonify
from app.vector_store import FAISSVectorStore
from app.rag_pipeline import run_rag

app = Flask(__name__)

print(" Loading FAISS index...")
store = FAISSVectorStore(dimension=384)
store.load()
print(" FAISS index loaded successfully")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "query" not in data:
            return jsonify({"error": "Query not provided"}), 400

        user_query = data["query"].strip()

        if not user_query:
            return jsonify({"error": "Empty query"}), 400

    
        result = run_rag(user_query, store)

        return jsonify({
            "answer": result["answer"],
            "sources": result["sources"]
        })

    except Exception as e:
        print(" Error:", str(e))
        return jsonify({
            "error": "Something went wrong",
            "details": str(e)
        }), 500



@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)