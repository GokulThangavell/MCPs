# qdrant/schema.py

from qdrant_client.http.models import VectorParams, Distance
from .client import client, COLLECTION_NAME

def create_collection_if_not_exists():
    if COLLECTION_NAME not in [c.name for c in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_cofig=VectorParams(size=384, distance=Distance.COSINE)
        )