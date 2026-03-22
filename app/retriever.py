import numpy as np
from app.embeddings import get_embedding

def retrieve(query, vector_store, k=2):
    query_embedding = get_embedding([query])
    query_embedding = np.array(query_embedding).astype("float32")

    return vector_store.search(query_embedding, k)