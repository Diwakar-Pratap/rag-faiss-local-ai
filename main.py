from app.embeddings import get_embedding
from app.vector_store import FAISSVectorStore
from app.chunking import chunk_text
from app.data_loader import load_from_folder


def build_index():
    folder = input("Enter folder path to index: ").strip()

    print("\n📂 Loading files...")
    texts = load_from_folder(folder)

    print(f"✅ Loaded {len(texts)} files")

    all_chunks = []
    sources = []

    print("\n✂️ Chunking data...")
    for file_path, text in texts:
        chunks = chunk_text(text, chunk_size=150)

        for chunk in chunks:
            all_chunks.append(chunk)
            sources.append(file_path)

    print(f"✅ Total chunks created: {len(all_chunks)}")

    # ⚠️ Optional limit (recommended for laptop)
    MAX_CHUNKS = 80000
    if len(all_chunks) > MAX_CHUNKS:
        print(f"⚠️ Limiting to first {MAX_CHUNKS} chunks for performance")
        all_chunks = all_chunks[:MAX_CHUNKS]
        sources = sources[:MAX_CHUNKS]

    store = FAISSVectorStore(dimension=384)

    print("\n🧠 Generating embeddings + indexing...")

    batch_size = 32

    for i in range(0, len(all_chunks), batch_size):
        batch_chunks = all_chunks[i:i + batch_size]
        batch_sources = sources[i:i + batch_size]

        embeddings = get_embedding(batch_chunks)

        store.add(embeddings, batch_chunks, batch_sources)

        print(f"📦 Indexed {i + len(batch_chunks)} / {len(all_chunks)}")

    print("\n💾 Saving FAISS index...")
    store.save()

    print("✅ Index built successfully!\n")

    return store


def load_index():
    print("\n📂 Loading existing FAISS index...")

    store = FAISSVectorStore(dimension=384)
    store.load()

    print("✅ Index loaded successfully!\n")

    return store


if __name__ == "__main__":
    print("🔧 RAG Index Builder")

    choice = input("\n1. Build Index\n2. Load Existing Index\nChoose: ").strip()

    if choice == "1":
        build_index()
    elif choice == "2":
        load_index()
    else:
        print("❌ Invalid choice")

    print("\n🚀 Now run Flask app (app.py) to query your data")