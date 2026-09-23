# Loads the sentence-transformer model and turns text into vector embeddings.

from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(texts):
    return model.encode(texts)
