from document_reader import read_document
from rag.rag_pipeline import build_index, search
from rag.embeddings import model
from rag.context_builder import build_context


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

context = build_context(results)

print("\nContext sent to LLM:")
print("--------------------")
print(context)
