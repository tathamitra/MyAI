import json


def save_chunks(chunks, path):
    with open(path, "w") as file:
        json.dump(chunks, file, indent=2)


def load_chunks(path):
    with open(path, "r") as file:
        return json.load(file)


def get_chunk(chunks, index):
    return chunks[index]
