import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.chunk_store import get_chunk


model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("docker.index")

question = "Docker volumes persist data."


# Convert question to vector using the same model used for indexing
question_embedding = model.encode([question])


# FAISS, take this question vector and find the 3 closest vectors you have.
distances, indexes = index.search(
    np.array(question_embedding).astype("float32"),
    3
)

print("\nRetrieved chunks:")

for rank, index_number in enumerate(indexes[0], start=1):
    chunk = get_chunk(index_number)

    print(f"\n{rank}. {chunk}")
    print("Distance:", distances[0][rank - 1])
