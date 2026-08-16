from utils.chunker import chunk_text

text = "A B C D E F G H I J K L"

chunks = chunk_text(
    text,
    chunk_size=10,
    overlap_words=3
)

for i, chunk in enumerate(chunks):
    print(f"CHUNK {i + 1}: {chunk}")
