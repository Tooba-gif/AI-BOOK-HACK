from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Dict, Optional
import uuid
from ..embedding.embedder import Embedder

class Retriever:
    def __init__(self, qdrant_url: str, collection_name: str = "textbook_content"):
        """
        Initialize the retriever with Qdrant client and collection name.
        """
        self.client = QdrantClient(url=qdrant_url)
        self.collection_name = collection_name
        self.embedder = Embedder()
        self._create_collection_if_not_exists()

    def _create_collection_if_not_exists(self):
        """
        Create the collection if it doesn't exist.
        """
        try:
            self.client.get_collection(self.collection_name)
        except:
            # Collection doesn't exist, create it
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
            )

    def add_document(self, content: str, chapter_id: str, section_title: str = "", metadata: Dict = None) -> str:
        """
        Add a document to the collection.
        """
        if metadata is None:
            metadata = {}

        doc_id = str(uuid.uuid4())
        vector = self.embedder.embed_text(content)

        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=doc_id,
                    vector=vector,
                    payload={
                        "content": content,
                        "chapter_id": chapter_id,
                        "section_title": section_title,
                        "metadata": metadata
                    }
                )
            ]
        )

        return doc_id

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Search for similar documents to the query.
        """
        query_embedding = self.embedder.embed_text(query)

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=top_k,
            with_payload=True
        )

        return [
            {
                "id": result.id,
                "content": result.payload["content"],
                "chapter_id": result.payload["chapter_id"],
                "section_title": result.payload["section_title"],
                "metadata": result.payload["metadata"],
                "score": result.score
            }
            for result in results
        ]