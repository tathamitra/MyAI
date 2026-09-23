from utils.chunk_store import load_chunks


chunks = load_chunks("chunks.json")

print("Chunks loaded.")
print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n{i}: {chunk}")
