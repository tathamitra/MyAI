from rag.embeddings import model
from rag.vector_store import load_index
from utils.chunk_store import load_chunks
from rag.retriever import retrieve


index = load_index("docker.index")

chunks = load_chunks("chunks.json")


question = "How can I keep my Docker data after deleting a container?"


results = retrieve(
    question,
    model,
    index,
    chunks,
    top_k=3
)


print("\nRetrieved chunks:")

for rank, result in enumerate(results, start=1):

    print(f"\n{rank}. {result['chunk']}")
    print("Distance:", result["distance"])
