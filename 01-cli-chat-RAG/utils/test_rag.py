import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from utils.chunk_store import get_chunk
from ai_client import ask_ai


model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("docker.index")


question = "How can I keep my Docker data after deleting a container?"


question_embedding = model.encode([question])


distances, indexes = index.search(
    np.array(question_embedding).astype("float32"),
    3
)


retrieved_chunks = []

for index_number in indexes[0]:
    retrieved_chunks.append(get_chunk(index_number))


context = "\n\n".join(retrieved_chunks)


prompt = f"""
You are a document question-answering assistant.

Answer the question using ONLY the information in the context below.

Do NOT use outside knowledge.

If the answer is not contained in the context, reply exactly:

"I could not find that information in the document."

Context:

{context}

Question:

{question}
"""


answer = ask_ai([
    {
        "role": "user",
        "content": prompt
    }
])


print("\nAnswer:")
print(answer)
