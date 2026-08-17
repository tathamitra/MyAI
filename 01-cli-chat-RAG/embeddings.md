# Day 8 — Embeddings

We have already built:

Document
   ↓
Chunking
   ↓
Chunks

Now we need to solve the next problem:

> How do we find which chunk is relevant to a user's question?

This is where **embeddings** come in.

---

## 1. The Problem

Imagine a document has 1,000 chunks:

Chunk 1 → Docker images
Chunk 2 → Kubernetes Pods
Chunk 3 → AWS IAM
...
Chunk 347 → Docker volumes
...
Chunk 1000 → GitHub Actions

The user asks:

> How can Docker keep my data after a container is deleted?

We don't want to send all 1,000 chunks to the LLM.

Instead, we want:

User question
   ↓
Find relevant chunks
   ↓
Chunk 347
   ↓
LLM
   ↓
Answer

The challenge is:

> How does the computer know that two pieces of text have similar meaning?

For example:

"How can Docker preserve my data?"

and:

"Docker volumes persist data."

The words are different, but the meaning is similar.

---

# 2. What Are Embeddings?

An **embedding** converts text into a numerical representation called a vector.

Conceptually:

"Docker volumes persist data"
            ↓
      Embedding model
            ↓
[0.12, -0.43, 0.87, 0.21, ...]

Another piece of text:

"How can Docker preserve my data?"
            ↓
      Embedding model
            ↓
[0.11, -0.40, 0.84, 0.25, ...]

These vectors should be relatively close because the two pieces of text have similar meaning.

---

# 3. Think of Embeddings as a Map

A useful mental model is:

> Embeddings place pieces of text into a mathematical space where semantically similar text tends to be close together.

Conceptually:

                 Kubernetes
                     ●

                              AWS IAM
                                ●


       Docker volumes ●
              ●
       Docker storage


                           GitHub Actions
                                  ●

The real embedding space has many dimensions.

The 2D diagram is only a visualization to make the concept easier to understand.

---

# 4. Why Embeddings Matter for RAG

We currently have:

Document
   ↓
Chunks

Embeddings add:

Chunks
   ↓
Embedding model
   ↓
Vectors

For example:

Chunk 1 → [0.12, 0.44, ...]
Chunk 2 → [0.87, 0.11, ...]
Chunk 3 → [0.21, 0.92, ...]

Later, we will store these vectors.

When the user asks a question:

"What are Docker volumes?"

the question is also converted into an embedding:

Question
   ↓
Embedding model
   ↓
Question vector

We then compare the question vector with the vectors of the document chunks.

The most similar chunks are considered relevant.

---

# 5. Embedding Model vs LLM

This distinction is extremely important.

## Embedding Model

Used primarily to represent and search for meaning.

Text
 ↓
Embedding model
 ↓
Vector

Purpose:

**Find relevant information.**

---

## LLM

Used primarily to generate the final answer.

Question + Relevant Context
          ↓
         LLM
          ↓
        Answer

Purpose:

**Generate the answer.**

---

## Simple Mental Model

Remember:

Embedding → Find relevant information

LLM → Generate the answer

---

# 6. RAG Architecture So Far

Our eventual RAG pipeline will look like:

Document
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Store
   ↓
User Question
   ↓
Question Embedding
   ↓
Similarity Search
   ↓
Relevant Chunks
   ↓
LLM
   ↓
Answer

We are building this one component at a time rather than jumping directly into a RAG framework.

---

# 7. Example

Suppose we have:

### Chunk A

Docker containers are isolated application environments.

### Chunk B

Docker volumes allow data to persist outside containers.

### Chunk C

Kubernetes Pods are the smallest deployable units in Kubernetes.

User asks:

> How can I persist data when using Docker?

The expected result is:

**Chunk B**

because its meaning is most closely related to the question.

---

# 8. Important Concept

Embeddings are not primarily about matching exact words.

Traditional keyword search might look for:

"Docker" + "persist" + "data"

Embeddings allow us to search based on **semantic similarity**.

For example:

User:

> How can I keep my files after my container disappears?

Document:

> Docker volumes provide persistent storage outside the container.

The wording is different, but the concepts are related.

That is one of the reasons embeddings are useful in RAG.

---
# Remember
Embedding = converting text into a fixed-size vector of numbers that represents its semantic characteristics.

And:

Vector length = how many numbers/dimensions that embedding contains.(depends on model) .

1 sentence
    ↓
all-MiniLM-L6-v2
    ↓
384 numbers
    ↓
1 vector
