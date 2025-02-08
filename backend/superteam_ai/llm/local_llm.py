from langchain.chains import RetrievalQA
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma

from ..document_processor.loader import DocumentLoader


class LocalLLM:
    def __init__(self, config):
        self.config = config
        self.llm = Ollama(model=config['model_name'])
        self.embeddings = OllamaEmbeddings(model=config['model_name'])
        self.document_loader = DocumentLoader()
        self.vector_store = None
        self.qa_chain = None

    def load_documents(self, file_paths):
        documents = []
        for file_path in file_paths:
            documents.extend(self.document_loader.load_document(file_path))
        
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.config.get('vector_store_path', './vector_store')
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever()
        )

    def generate_response(self, prompt):
        if not self.qa_chain:
            raise ValueError("Documents must be loaded first using load_documents()")
        
        response = self.qa_chain.run(prompt)
        return response


if __name__ == "__main__":
    config = {
        'model_name': 'deepseek-r1:1.5b',
        'vector_store_path': './vector_store'
    }
    llm = LocalLLM(config)
    llm.load_documents(["./data/sample.pdf"])
    response = llm.generate_response("What is the purpose of this document?")
    print(response)