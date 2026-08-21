from document_reader import read_document
from rag.rag_pipeline import build_index


document = read_document("docs/docker.md")

chunks, index = build_index(document)

print("\nNumber of chunks:", len(chunks))
print("Number of vectors:", index.ntotal)

print("\nChunks:")

for i, chunk in enumerate(chunks):
    print(f"\n{i}: {chunk}")
