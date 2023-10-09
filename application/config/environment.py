"""環境変数の読み込み."""

from typing import List

from pydantic_settings import BaseSettings


class VariableSettings(BaseSettings):
    """環境変数を取得する設定クラス."""

    DEBUG: bool = True
    """DEBUGモードで起動（True）"""

    TRUSTED_ORIGINS: List[str] = ["http://localhost:3000"]
    """CORSで許可するオリジン"""
    # CSRF_COOKIE_DOMAIN: str = ""
    """CSRFCookieを設定するときに使用されるドメイン"""

class PostgresSettings(BaseSettings):
    """Postgres絡みの設定クラス."""

    POSTGRES_NAME: str
    """PostgreSQLのデータベース名"""
    POSTGRES_USER: str
    """PostgreSQLのユーザ名"""
    POSTGRES_PASSWORD: str
    """PostgreSQLのパスワード"""
    POSTGRES_HOST: str
    """PostgreSQLのホスト名"""
    POSTGRES_PORT: int
    """PostgreSQLのポート番号"""


settings = VariableSettings()
"""環境変数"""

postgres_settings = PostgresSettings()
"""postgres絡みの環境変数"""
