# app.model.py
"""Глобальный синглтон SentenceTransformer + загрузка при старте."""
import logging

import torch
from sentence_transformers import SentenceTransformer

from app.config import settings

logger = logging.getLogger(__name__)

_model: SentenceTransformer | None = None


def load_model() -> None:
    global _model
    torch.set_num_threads(settings.cpu_threads)
    torch.use_deterministic_algorithms(True)

    logger.info("Загружаю модель из %s (CPU, threads=%d)",
                settings.model_dir, settings.cpu_threads)
    _model = SentenceTransformer(
        settings.model_dir,
        device="cpu",
        local_files_only=True,
    )
    _model.eval()
    logger.info("Модель загружена (dim=%d)",
                _model.get_sentence_embedding_dimension())


def get_model() -> SentenceTransformer:
    if _model is None:
        raise RuntimeError("Модель не загружена (load_model не вызван)")
    return _model


def get_dim() -> int:
    return get_model().get_sentence_embedding_dimension()