# app.main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.model import load_model
from app.routers.embed import router as embed_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()          # один раз при старте
    yield
    # (опционально) cleanup


app = FastAPI(title="embedder", lifespan=lifespan)
app.include_router(embed_router)