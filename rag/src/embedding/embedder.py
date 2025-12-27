from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List

class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the embedder with a pre-trained sentence transformer model.
        """
        self.model = SentenceTransformer(model_name)
    
    def embed_text(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.
        """
        embedding = self.model.encode([text])
        return embedding[0].tolist()  # Convert to list for JSON serialization
    
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        """
        embeddings = self.model.encode(texts)
        return [embedding.tolist() for embedding in embeddings]
    
    def similarity(self, embedding1: List[float], embedding2: List[float]) -> float:
        """
        Calculate cosine similarity between two embeddings.
        """
        emb1 = np.array(embedding1)
        emb2 = np.array(embedding2)
        cosine_sim = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
        return float(cosine_sim)