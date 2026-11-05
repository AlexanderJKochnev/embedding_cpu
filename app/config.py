# app.config.py
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model_dir: str = os.getenv("LABSE_LOCAL_DIR", "/app/models/LaBSE-ru-turbo")
    cpu_threads: int = int(os.getenv("LABSE_CPU_THREADS", "4"))
    vector_dtype: str = os.getenv("VECTOR_DTYPE", "float16")
    batch_size: int = int(os.getenv("EMBED_BATCH_SIZE", "64"))


settings = Settings()