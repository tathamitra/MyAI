                         ┌──────────────┐
                         │   Document   │
                         └──────┬───────┘
                                ↓
                             Chunks
                                ↓
                           Embeddings
                                ↓
                            FAISS
                                ↑
                                │
Question ──→ Embedding ──→ Search
                                ↓
                         Relevant chunks
                                ↓
                       Grounded prompt
                                ↓
                              LLM
                                ↓
                             Answer
