# app.crud.py
"""Embedding-логика. Единственное место, где вызывается model.encode()."""
import numpy as np

from app.config import settings
from app.model import get_model


def embed_texts(texts: list[str]) -> tuple[list[list[float]], str]:
    """
    Возвращает (vectors, dtype). Векторы — JSON-safe (float32),
    dtype — исходный ('float16'/'float32'), чтобы клиент знал, как упаковывать.
    """
    if not texts:
        return [], settings.vector_dtype

    vecs = get_model().encode(
        texts,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=False,
        batch_size=settings.batch_size,
    )

    # JSON не умеет float16 — отдаём float32, клиент сам упакует в нужный dtype.
    return vecs.astype(np.float32).tolist(), settings.vector_dtype