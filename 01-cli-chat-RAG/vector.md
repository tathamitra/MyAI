#  Important Concept
Embedding = the meaning representation produced by the model.

Vector = the mathematical representation used to store that embedding.

Text
 ↓
Embedding model
 ↓
Embedding
 ↓
[0.011, 0.034, -0.024, ...]
       ↑
     Vector

## Example

embedding = model.encode(
    "Docker volumes persist data."
)

embedding is the resulting representation.

When you print it, you see something like:

[0.0110018, 0.03409806, -0.02449758, ...]

That array of numbers is the vector.

## so
| Term                 | Think of it as                                      |
| -------------------- | --------------------------------------------------- |
| **Embedding**        | The semantic representation created by the model    |
| **Vector**           | The mathematical structure containing those numbers |
| **Embedding vector** | Both together                                       |


Chunking answers:

"How do I break my document into manageable pieces?"

Embedding answers:

"How do I represent the meaning of each piece numerically?"

Vector similarity answers:

"Which pieces are most relevant to this question?"

LLM answers:

"Given those relevant pieces, how do I formulate the answer?"

## so when user questions that is also chunked and converted to a vector and then compared to
## rest of vectors to find mist similar ones

chunks
 ↓
embeddings
 ↓
user question
 ↓
question embedding
 ↓
similarity
 ↓
top matching chunk

## Definition
A vector index is a data structure that makes finding similar vectors efficient.

A vector database is a system that stores vectors and usually provides:

similarity search
metadata
persistence
filtering
APIs
indexing

# Sentence Transformers → creates embeddings
'''from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embedding = model.encode("Docker volumes persist data.")'''
This is the model that turns text → meaning-numbers (embeddings).
Input: a sentence/chunk of text.
Output: a vector (384 numbers for MiniLM).
Its only job: understand language and represent meaning numerically. It does not store or search anything.

# NumPy → holds/manipulates the numerical vectors
'''
import numpy as np
vectors = np.array(embeddings)   # shape: (num_chunks, 384)
'''
NumPy is the container and math engine for those vectors.
Its only job: efficiently store and manipulate arrays of numbers. It doesn't understand text, and for large data its search is brute-force (slow).
# FAISS → indexes/searches those vectors
import faiss
index = faiss.IndexFlatL2(384)   # build an index for 384-dim vectors
index.add(vectors)               # store all chunk vectors
distances, ids = index.search(question_vector, k=3)  # find 3 nearest
FAISS (Facebook AI Similarity Search) is built for fast similarity search over many vectors.
It builds a special index data structure so it can find the nearest vectors without comparing against every single one (which is what plain NumPy would do).
Its only job: given a query vector, quickly return the most similar stored vectors.

Imagine two vectors as points in space:

                Vector B
                   ●
                  /
                 /
                /
               ●
          Vector A

L2 distance asks:

How far apart are these two vectors?

Smaller distance means they're closer.

FAISS is effectively doing:

Question vector
       │
       ├── distance → Chunk 0
       ├── distance → Chunk 1
       ├── distance → Chunk 2
       ├── distance → Chunk 3
       └── distance → Chunk 4

Then it returns the closest ones.


## final flow

DOCUMENT
                    │
                    ▼
                 CHUNKS
                    │
                    ▼
              EMBEDDING MODEL
                    │
                    ▼
               384 numbers
                    │
                    ▼
                FAISS
             ┌─────────────┐
             │ Vector 0    │
             │ Vector 1    │
             │ Vector 2    │
             │ Vector 3    │
             │ Vector 4    │
             └─────────────┘
                    ▲
                    │
              QUESTION
                    │
                    ▼
              384 numbers
                    │
                    ▼
              FAISS SEARCH
                    │
                    ▼
             TOP 3 VECTORS
                    │
                    ▼
              ACTUAL CHUNKS
