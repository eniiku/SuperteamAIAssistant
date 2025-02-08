import os
import shutil
import warnings

from chromadb.config import Settings
from langchain.chains import RetrievalQA
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from superteam_ai.document_processor.loader import DocumentLoader

warnings.filterwarnings("ignore")



class LocalLLM:
    def __init__(self, config):
        self.config = config
        self.llm = Ollama(model=config['model_name'])
        # Use a specific embedding model (e.g., nomic-embed-text) for consistent dimensions
        self.embeddings = OllamaEmbeddings(model=config.get('embedding_model_name', 'nomic-embed-text'), )
        self.document_loader = DocumentLoader()
        self.vector_store = None
        self.qa_chain = None
        self.vector_store_path = config.get('vector_store_path', './vector_store')
        self.chroma_settings = Settings(
            anonymized_telemetry=False,
            allow_reset=True,
            is_persistent=True
        )
        self.conversation_history = []  # new attribute to keep conversation context

    def _clear_vector_store(self):
        if os.path.exists(self.vector_store_path):
            shutil.rmtree(self.vector_store_path)

    def load_documents(self, file_paths):
        # Clear existing vector store to avoid dimension conflicts
        self._clear_vector_store()
        
        documents = []
        for file_path in file_paths:
            documents.extend(self.document_loader.load_document(file_path))
        
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.vector_store_path,
            collection_metadata={"dimension": 4096},
            client_settings=self.chroma_settings
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever()
        )

    def generate_response(self, prompt):
        if not self.qa_chain:
            raise ValueError("Documents must be loaded first using load_documents()")
        
        response = self.qa_chain.invoke(prompt)
        return response

    def conversation_turn(self, user_input):
        # Append user input to conversation history
        self.conversation_history.append(f"User: {user_input}")
        # Build conversation prompt with existing context, keeping only the last N turns if desired
        # For simplicity, we're using full context
        conversation_prompt = "\n".join(self.conversation_history) + "\nBot:"
        response = self.generate_response(conversation_prompt)
        self.conversation_history.append(f"Bot: {response}")
        return response


if __name__ == "__main__":
    config = {
        'model_name': 'llama3.1',
        'embedding_model_name': 'nomic-embed-text',
        'vector_store_path': './vector_store'
    }
    llm = LocalLLM(config)
    llm.load_documents(["./data/sample.pdf"])
    response = llm.generate_response("What is the purpose of this document?")
    print(response)

