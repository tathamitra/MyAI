# Embeds a question and retrieves the most similar chunks from the FAISS index.

import numpy as np


def retrieve(question, model, index, chunks, top_k=3):

    question_embedding = model.encode([question])

    actual_k = min(top_k, index.ntotal)

    distances, indexes = index.search(
        np.array(question_embedding).astype("float32"),
        actual_k
    )

    results = []

    for distance, index_number in zip(distances[0], indexes[0]):

        if index_number == -1:
            continue

        results.append(
            {
                "chunk": chunks[index_number],
                "distance": distance
            }
        )

    return results
