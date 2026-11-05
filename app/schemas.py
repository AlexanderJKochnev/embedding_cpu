# app.schemas.py
from typing import List
from pydantic import BaseModel, Field


class EmbedRequest(BaseModel):
    texts: List[str] = Field(..., max_length=512)


class EmbedResponse(BaseModel):
    vectors: List[List[float]]
    dim: int
    dtype: str


class HealthResponse(BaseModel):
    status: str
    dim: int