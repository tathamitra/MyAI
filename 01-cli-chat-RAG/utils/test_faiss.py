import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


chunks = [
    "Docker is a container platform.",
    "Docker images are blueprints for containers.",
    "Containers are running instances of images.",
    "Volumes persist data.",
    "Networks allow containers to communicate."
]


embeddings = model.encode(chunks)

print("Embedding shape:", embeddings.shape)


dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))

print("Number of vectors in index:", index.ntotal)


# save the index to a file in other words  here we are persisting the index to a file so that we can load it later and use it for searching
faiss.write_index(index, "docker.index")

print("FAISS index saved.")

question1 = "How can I keep my Docker data after deleting a container?"


question_embedding1 = model.encode([question1])


distances1, indexes1 = index.search(
    np.array(question_embedding1).astype("float32"),
    3
)


print("\nIndexes for question 1:")
print(indexes1)

print("\nDistances for question 1:")
print(distances1)




print("\nResults for question 1:")
for rank, index_number in enumerate(indexes1[0], start=1):
    print(f"\n{rank}. {chunks[index_number]}")

## Tried with another Question
#--------------------------------

#question2 = "Docker volumes persist data."
#question_embedding2 = model.encode([question2])
#distances2, indexes2 = index.search(
#   np.array(question_embedding2).astype("float32"),
#    3
#)
# print(indexes2)
# print(distances2)
# print("\nIndexes for question 2:")
#print("\nDistances for question 2:")
##print("\nResults for question 2:")
##for rank, index_number in enumerate(indexes2[0], start=1):
##    print(f"\n{rank}. {chunks[index_number]}")

## Another vector 4th  was selected as its distance was least.(it was the closest vector to the question vector)
#--------------------------
