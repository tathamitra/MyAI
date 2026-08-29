from document_reader import read_document
from rag.chunker import chunk_text
from rag.embeddings import create_embeddings
from rag.vector_store import create_index, save_index


document = read_document("docs/docker.md")

chunks = chunk_text(document)

embeddings = create_embeddings(chunks)

index = create_index(embeddings)

save_index(index, "docker.index")

print("Index saved.")
print("Number of vectors:", index.ntotal)
