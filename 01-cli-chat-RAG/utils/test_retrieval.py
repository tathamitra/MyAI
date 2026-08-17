from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


chunks = [
    "Docker is a container platform.",
    "Docker images are blueprints for containers.",
    "Containers are running instances of images.",
    "Volumes persist data.",
    "Networks allow containers to communicate."
]


chunk_embeddings = model.encode(chunks)


question = "How can I keep my Docker data after deleting a container?"

question_embedding = model.encode(question)

similarities = cosine_similarity(
    [question_embedding],
    chunk_embeddings
)[0]

print(similarities)

best_index = similarities.argmax()

print("\nBest matching chunk:")
print(chunks[best_index])

print("Similarity:", similarities[best_index])

top_indexes = similarities.argsort()[::-1][:3]

print("\nTop 3 matching chunks:")
for rank, index in enumerate(top_indexes, start=1):
    print(f"\n{rank}. {chunks[index]}")
    print("Similarity:", similarities[index])
