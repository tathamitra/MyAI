# MyAI — RAG Learning Project

This project is my hands-on journey toward building AI agents and RAG-based applications using Python and LLMs.

The project is built incrementally. Each stage introduces one important AI engineering concept.

---

# Current Progress

- Day 1 — Basic LLM CLI
- Day 2 — Conversation / Message History
- Day 3 — Streaming Responses
- Day 4 — AI Personas / Prompt Engineering
- Day 5 — Document Assistant
- Day 6 — Understanding the limitations of sending entire documents
- Day 7 — Document Chunking + Chunk Overlap
- Day 8 — Embeddings (next)

---

# 1. Day 1 — Basic LLM CLI

## Goal

Build a simple Python CLI application that sends a question to an LLM and prints the response.

Initial architecture:

```text
User
 ↓
Python application
 ↓
Groq API
 ↓
LLM
 ↓
Response
```

---

#  Day 2 — Basic LLM CLI

## Goal

Introduce a `messages` list so the app remembers the whole conversation.


See [`app.py` lines 31–36](app.py#L31-L36):

See [`app.py` lines 75–80](app.py#L75-L80):

See [`app.py` lines 86–91](app.py#L86-L91):

#  Day 3 — Streaming Responses

## Goal

Instead of waiting for the complete response, stream it chunk by chunk as it is generated.

### 1. Enable streaming on the API call
See [`ai_client.py` lines 11–15](ai_client.py#L11-L15):

### 2. Process each streamed chunk
See [`ai_client.py` lines 18–23](ai_client.py#L18-L23):

Each chunk's text is printed immediately with `flush=True`, creating the live "typing" effect, while also being appended to `full_response`.
