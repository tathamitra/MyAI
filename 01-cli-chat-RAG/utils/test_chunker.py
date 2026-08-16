from utils.chunker import chunk_text

text = """
Docker is a container platform.

Docker images are blueprints for containers.

Containers are running instances of images.

Volumes persist data.

Networks allow containers to communicate.
"""

chunks = chunk_text(text, chunk_size=50)

for i, chunk in enumerate(chunks):
    print(f"\n--- CHUNK {i + 1} ---")
    print(chunk)
