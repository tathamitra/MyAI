from rag.chunker import chunk_text
from rag.embeddings import model, create_embeddings
from rag.vector_store import create_index
from rag.retriever import retrieve

def build_index(document):

    chunks = chunk_text(document)

    embeddings = create_embeddings(chunks)

    index = create_index(embeddings)

    return chunks, index


def search(question, model, index, chunks, top_k=3):

    return retrieve(
        question,
        model,
        index,
        chunks,
        top_k
    )
