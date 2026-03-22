import os 
from dotenv import load_dotenv

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

FAISS_INDEX_PATH = "faiss_index/index.bin"
METADATA_PATH = "faiss_index/metadata.pkl"
