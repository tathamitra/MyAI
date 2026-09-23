from pathlib import Path


def read_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    return path.read_text(encoding="utf-8")
