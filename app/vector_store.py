import faiss
import numpy as np
import pickle
import os
from app.config import FAISS_INDEX_PATH, METADATA_PATH

class FAISSVectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)
        self.metadata = []  # list of dicts

    def add(self, embeddings, docs, sources):
        faiss.normalize_L2(embeddings)
        for i in range(len(docs)):
            self.metadata.append({
                "text": docs[i],
                "source": sources[i]
            })

        self.index.add(np.array(embeddings).astype("float32"))

    def search(self, query_embedding, k=3):
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for i in indices[0]:
            if i == -1:
                continue

            if i < len(self.metadata):
                results.append(self.metadata[i])

        return results

    def save(self):
        os.makedirs("faiss_index", exist_ok=True)
        faiss.write_index(self.index, FAISS_INDEX_PATH)

        with open(METADATA_PATH, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self):
        self.index = faiss.read_index(FAISS_INDEX_PATH)

        with open(METADATA_PATH, "rb") as f:
            self.metadata = pickle.load(f)