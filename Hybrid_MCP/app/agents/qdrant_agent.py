from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance
from app.embeddings.embedder import get_embedding

qdrant = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "hybrid_mcp"

def init_collection():
    if COLLECTION_NAME not in qdrant.get_collections().collections:
        qdrant.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

def add_document(doc_id: int, text: str, metadata:dict):
    vector = get_embedding(text)
    point = PointStruct(id=doc_id, vector=vector, payload=metadata)
    qdrant.upsert(collection_name=COLLECTION_NAME, points=[point])

def delete_document(doc_id:int):
        qdrant.delete(collection_name= COLLECTION_NAME, points_selector={"points":[doc_id]})

def update_document(doc_id: int, text:str, metadata = dict):
     add_document(doc_id, text, metadata)

def list_documents(limit: int=100):
     """Return a list of all documents(IDs, vectors, and payloads)."""
     result = qdrant.scroll(
          collection_name= COLLECTION_NAME,
          limit=limit,
          with_vectors=False,
          with_payload=True
     )
     return