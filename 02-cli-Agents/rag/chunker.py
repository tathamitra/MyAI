# Splits raw document text into overlapping word-based chunks for embedding.


def chunk_text(text, chunk_size=20, overlap_words=10):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        # Calculate the end index for the current chunk, ensuring it does not exceed the total number of words
        end = min(start + chunk_size, len(words))

        chunk = words[start:end]
        chunks.append(" ".join(chunk))

        if end == len(words):
            break

        start = end - overlap_words

    return chunks
