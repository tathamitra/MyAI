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
