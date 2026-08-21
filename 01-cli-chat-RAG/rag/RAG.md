| File              | Job                                 |
| ----------------- | ----------------------------------- |
| `chunker.py`      | Break document into chunks          |
| `embeddings.py`   | Turn chunks into vectors            |
| `vector_store.py` | Put vectors into FAISS              |
| `retriever.py`    | Find relevant chunks for a question |
| `rag_pipeline.py` | **Orchestrate everything**          |



rag/
   = "What my application does"

utils/
   = "Things I use to test/check my application"
