from rag.vector_store import load_index


index = load_index("docker.index")

print("Index loaded.")
print("Number of vectors:", index.ntotal)
