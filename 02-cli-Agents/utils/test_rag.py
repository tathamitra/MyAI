from document_reader import read_document
from rag.rag_pipeline import build_index, ask_rag
from rag.embeddings import model


document = read_document("docs/docker.md")

chunks, index = build_index(document)

question = "How can I keep my Docker data after deleting a container?"

answer = ask_rag(
    question,
    model,
    index,
    chunks,
    top_k=3
)

print("\nAnswer:")
print(answer)
