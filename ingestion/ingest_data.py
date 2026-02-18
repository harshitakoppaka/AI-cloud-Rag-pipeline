from pathlib import Path
from PyPDF2 import PdfReader

def load_documents(data_path="data"):
    documents = []

    data_dir = Path(data_path)

    for file in data_dir.iterdir():
        if file.suffix == ".pdf":
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            documents.append(text)

        elif file.suffix == ".txt":
            with open(file, "r", encoding="utf-8") as f:
                documents.append(f.read())

    print(f"Loaded {len(documents)} documents successfully.")
    return documents


if __name__ == "__main__":
    load_documents()
