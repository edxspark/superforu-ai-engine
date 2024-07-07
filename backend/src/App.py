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


# Chat
@app.post('/v1/chat/completions')
async def completions():
    return {'status': 'completions'}


# Embedding file
@app.post("/v1/embeddings")
def embeddings():
    return {'status': 'document_to_vector_db'}


#
@app.post("/file/content/related")
def get_related_content():
    return {'status': 'get_related_content'}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=11888)
