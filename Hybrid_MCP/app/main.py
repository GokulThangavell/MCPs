from fastapi import FastAPI
from pydantic import BaseModel
from app.agents import qdrant_agent

app = FastAPI()

qdrant_agent.init_collection()

class Document(BaseModel):
    doc_id:int
    text:str
    metadata:dict={}

@app.post("/add")
def add_doc(doc: Document):
    qdrant_agent.add_document(doc.doc_id, doc.text, doc.metadata)
    return {"status":"Document added"}

@app.put("/update")
def update_doc(doc:Document):
    qdrant_agent.update_document(doc.doc_id, doc.text, doc.metadata)
    return {"status":"Document updated"}

@app.delete("/delete/{doc_id}")
def delete_doc(doc_id:int):
    qdrant_agent.delete_document(doc_id)
    return {"status":"Document deleted"}

@app.get("/list-document")
def list_documents(limit: int=100):
    result = qdrant_agent.list_documents(limit)
    if result:
        return {"count":len(result[0]), "documents":result[0]}
    else:
        return {"Document is empty"}