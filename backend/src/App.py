#!/usr/bin/venv python

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Superforu AI Engine",
    version="1.0",
    description="SuperforuAIEngine is a data engine for your LLM application. ",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/v1/chat/completions')
async def completions():
    return {'status': 'completions'}


@app.post("/ai/embedding/get_related_content")
def get_related_content():
    return {'status': 'get_related_content'}


@app.post("/ai/embedding/document_to_vector_db")
def document_to_vector_db():
    return {'status': 'document_to_vector_db'}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10101)
