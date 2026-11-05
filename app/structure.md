embedder/
├── Dockerfile
├── requirements.txt
└── app/
    ├── __init__.py
    ├── main.py            ← FastAPI, lifespan, подключение роутера
    ├── config.py          ← настройки (MODEL_DIR, CPU_THREADS, dtype)
    ├── model.py           ← глобальный синглтон модели + загрузка
    ├── schemas.py         ← pydantic-модели запроса/ответа
    ├── crud.py            ← embed(texts) → list[list[float]]
    └── routers/
        ├── __init__.py
        └── embed.py       ← POST /embed, GET /health