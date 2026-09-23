from rag.chunker import chunk_text
from rag.embeddings import model, create_embeddings
from rag.vector_store import create_index
from rag.retriever import retrieve
from rag.context_builder import build_context
from ai_client import ask_ai


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


def ask_rag(question, model, index, chunks, top_k=3):

    results = search(
        question,
        model,
        index,
        chunks,
        top_k
    )

    context = build_context(results)

    messages = [
        {
            "role": "system",
            "content": (
                "Answer the question using only the provided context. "
                "If the answer is not in the context, say "
                "\"I could not find that information in the document.\""
            )
        },
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{question}
"""
        }
    ]

    return ask_ai(messages)
