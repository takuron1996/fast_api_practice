"""環境変数の読み込み."""

from typing import List

from pydantic_settings import BaseSettings

# from enum import Enum

# class RunEnvEnum(Enum):
#     """実行環境の一覧"""
#     LOCAL = "local"
#     """ローカル環境"""
#     TEST = "test"
#     """テスト環境"""

class VariableSettings(BaseSettings):
    """環境変数を取得する設定クラス."""

    # RUN_ENV: RunEnvEnum = RunEnvEnum.LOCAL
    """実行環境"""
    TRUSTED_ORIGINS: List[str] = ["http://localhost:3000"]
    """CORSで許可するオリジン"""
    # CSRF_COOKIE_DOMAIN: str = ""
    """CSRFCookieを設定するときに使用されるドメイン"""



settings = VariableSettings()
"""環境変数"""
