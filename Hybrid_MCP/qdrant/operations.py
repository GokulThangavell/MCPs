# qdrant/operations.py

from uuid import uuid4
from .client import client, COLLECTION_NAME

def add_document(vector:list[float], payload:dict) -> str:
    doc_id=str(uuid4())
    client.upsert(
        collection_name=COLLECTION_NAME,
        points = [
            {
                "id":doc_id,
                "vector":vector,
                "payload":payload
            }
        ]
    )
    return doc_id

def update_document(doc_id:str, new_vector:list[float], new_payload:dict):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points = [{
             "id":doc_id,
                "vector":new_vector,
                "payload":new_payload
        }]
    )

    def delete_document(doc_id: str):
        client.delete(
            collection_name = COLLECTION_NAME,
            points_selector = {"points": [doc_id]}
        )