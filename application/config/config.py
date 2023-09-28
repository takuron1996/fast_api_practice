"""全環境での設定を記述."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.environment import settings


def setup_middlewares(app: FastAPI) -> None:
    """ミドルウェアの設定を適応."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.TRUSTED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
