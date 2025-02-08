import json

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import Docx2txtLoader, PyPDFLoader


class DocumentLoader:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )

    def load_document(self, file_path):
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            return loader.load_and_split(self.text_splitter)
        elif file_path.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
            return loader.load_and_split(self.text_splitter)
        elif file_path.endswith(".json"):
            with open(file_path, "r") as f:
                data = json.load(f)
            # Convert JSON to string and split
            text = json.dumps(data, indent=2)
            return self.text_splitter.split_text(text)
