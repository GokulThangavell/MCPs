#qdrant/client.py

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
import os

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION_NAME = "mcp_collection"

client = QdrantClient(url=QDRANT_URL)
