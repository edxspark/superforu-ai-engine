from pydantic import BaseModel
from typing import Optional


class EmbeddingBo(BaseModel):
    agentType: str
    fileType: str
    kmId: str
    fileId: str
    fileName: str
    fileContent: str
    fileURL: str

class RelatedContentBo(BaseModel):
    agentType: str
    question: str
    kmId: str

class ChatBo(BaseModel):
    messages: list
    stream: bool
    model: str
    temperature: float
    presence_penalty: float
    frequency_penalty: float
    top_p: int
    agent_type: Optional[str] = None
    km_id: Optional[str] = None
    user_id: Optional[str] = None
    session_id: Optional[str] = None
