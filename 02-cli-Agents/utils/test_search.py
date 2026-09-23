from document_reader import read_document
from rag.rag_pipeline import build_index, search
from rag.embeddings import model


document = read_document("docs/docker.md")

chunks, index = build_index(document)

question = "How can I keep my Docker data?"

results = search(
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
