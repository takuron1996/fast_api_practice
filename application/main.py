"""FastAPIのエントリーポイント."""


from fastapi import FastAPI

from config.config import setup_middlewares
from routers import router

app = FastAPI()
"""FastAPIのインスタンス"""

setup_middlewares(app)

app.include_router(router)
