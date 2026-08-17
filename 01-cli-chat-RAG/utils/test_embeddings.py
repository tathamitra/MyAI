from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):
    return model.encode(text)


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
