from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


# Creates embedding.
# Every embedding is a vector, but not every vector is an embedding. An embedding is a vector with meaning baked in.
# The word "embedding" refers to the fact that the text is "embedded" (placed) into a numeric space where similar meanings sit close together

def create_embedding(text):
    return model.encode(text) # .encode(text) is the method that turns text into numbers.


texts = [
    "Docker volumes persist data.",
    "How can I keep my data after deleting a Docker container?",
    "Kubernetes Pods are the smallest deployable units."
]


embeddings = [create_embedding(text) for text in texts]


for text, embedding in zip(texts, embeddings):
    print("\nText:", text)
    print("Vector length:", len(embedding))

similarity_1_2 = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]

similarity_1_3 = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)[0][0]

print("\nSimilarity:")
print("Docker ↔ Docker:", similarity_1_2)
print("Docker ↔ Kubernetes:", similarity_1_3)
