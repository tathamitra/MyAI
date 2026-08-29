INGESTION
Document → Chunks → Embeddings → FAISS → Save
                                      ↓
                                   Knowledge
                                    Base

QUERY
Question → Embedding → FAISS Search → Chunks → LLM → Answer
