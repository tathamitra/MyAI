from document_reader import read_document
from rag.chunker import chunk_text
from utils.chunk_store import save_chunks


document = read_document("docs/docker.md")

chunks = chunk_text(document)

save_chunks(chunks, "chunks.json")

print("Chunks saved.")
print("Number of chunks:", len(chunks))
