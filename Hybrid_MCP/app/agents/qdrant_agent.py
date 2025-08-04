from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance
from app.embeddings.embedder import get_embedding
from qdrant_client.models import PointIdsList

qdrant = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "hybrid_mcp"

def init_collection():
      existing_collections = [col.name for col in qdrant.get_collections().collections] 
      if COLLECTION_NAME not in existing_collections:
        qdrant.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )
        
#def init_collection():
#    if COLLECTION_NAME not in qdrant.get_collections().collections:
#        qdrant.recreate_collection(
#            collection_name=COLLECTION_NAME,
#            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
#        )

def add_document(doc_id: int, text: str, metadata:dict):
    vector = get_embedding(text)
    
    payload = {
        "text": text,
        "metadata":metadata
    }

    point = PointStruct(id=doc_id, vector=vector, payload=metadata)
    qdrant.upsert(collection_name=COLLECTION_NAME, points=[point])

def delete_document(doc_id:int):
        qdrant.delete(collection_name= COLLECTION_NAME,points_selector=PointIdsList(points=[doc_id]))
                       #points_selector={"points":[doc_id]})

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
     return  result