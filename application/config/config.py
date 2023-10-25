"""全環境での設定を記述."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from config.environment import postgres_settings, settings


def setup_middlewares(app: FastAPI) -> None:
    """ミドルウェアの設定を適応."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.TRUSTED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


class SessionFactory:
    """非同期のセッション生成用のファクトリ."""

    @staticmethod
    def get_url(drivername="postgresql+asyncpg"):
        """接続先のURLを返却."""
        return URL.create(
            drivername=drivername,
            username=postgres_settings.POSTGRES_USER,
            password=postgres_settings.POSTGRES_PASSWORD,
            host=postgres_settings.POSTGRES_HOST,
            database=postgres_settings.POSTGRES_NAME,
            port=postgres_settings.POSTGRES_PORT,
        )

    @classmethod
    def create(cls):
        """セッションを生成."""
        if not hasattr(cls, "_session_factory"):
            engine = create_async_engine(cls.get_url(), echo=settings.DEBUG)
            cls._session_factory = async_sessionmaker(
                autocommit=False,
                autoflush=False,
                expire_on_commit=False,
                bind=engine,
            )
        return cls._session_factory


async def get_async_session():
    """DBの非同期セッションインスタンスを返却."""
    async_session = SessionFactory.create()
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
