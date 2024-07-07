#!/usr/bin/venv python

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.src.com.domain.app.bo.AppBo import ChatBo, EmbeddingBo, RelatedContentBo

app = FastAPI(
    title="superforu-ai-engine",
    version="1.0",
    description="An AI data engine for build RAG and Agent.",
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
async def completions(chatBo: ChatBo):
    return {'status': 'completions'}


# Embedding file
@app.post("/v1/embeddings")
def embeddings(embeddingBo: EmbeddingBo):
    return {'status': 'document_to_vector_db'}


#
@app.post("/file/content/related")
def get_related_content(relatedContentBo: RelatedContentBo):
    return {'status': 'get_related_content'}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=11888)
