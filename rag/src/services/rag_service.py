from typing import List, Dict
from .retrieval.retriever import Retriever
from .generation.generator import Generator
from .config.settings import settings

class RAGService:
    def __init__(self):
        """
        Initialize the RAG service with retriever and generator.
        """
        self.retriever = Retriever(
            qdrant_url=settings.qdrant_url,
            collection_name="textbook_content"
        )
        self.generator = Generator()
    
    def answer_question(self, question: str, top_k: int = 5) -> Dict:
        """
        Answer a question using the RAG approach.
        """
        # Retrieve relevant documents
        context = self.retriever.search(question, top_k=top_k)
        
        # Generate answer with citations
        result = self.generator.generate_answer_with_citations(question, context)
        
        return result
    
    def add_content_to_kb(self, content: str, chapter_id: str, section_title: str = "", metadata: Dict = None) -> str:
        """
        Add content to the knowledge base for retrieval.
        """
        doc_id = self.retriever.add_document(content, chapter_id, section_title, metadata)
        return doc_id