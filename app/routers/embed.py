# app.routers.embed.py
from fastapi import APIRouter, HTTPException

from app.crud import embed_texts
from app.model import get_dim
from app.schemas import EmbedRequest, EmbedResponse, HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health():
    try:
        return HealthResponse(status="ok", dim=get_dim())
    except Exception:
        raise HTTPException(503, "model not loaded")


@router.post("/embed", response_model=EmbedResponse)
async def embed(req: EmbedRequest):
    try:
        vectors, dtype = embed_texts(req.texts)
    except Exception as e:
        raise HTTPException(500, f"embed failed: {e}")
    return EmbedResponse(vectors=vectors, dim=get_dim(), dtype=dtype)