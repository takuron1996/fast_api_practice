"""FastAPIのエントリーポイント."""
from typing import Dict

from fastapi import FastAPI

from config.config import setup_middlewares

app = FastAPI()
"""FastAPIのインスタンス"""

setup_middlewares(app)

@app.get("/")
async def root() -> Dict[str, str]:
    """ルートパス.

    Returns:
        messeageを返却
    """
    return {"message": "Hello World"}
