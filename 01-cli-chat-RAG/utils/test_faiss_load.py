import faiss

index = faiss.read_index("docker.index")

print("Loaded vectors:", index.ntotal)
