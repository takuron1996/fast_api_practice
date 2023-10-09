"""バリデーションをまとめたモジュール."""

from pydantic.functional_validators import AfterValidator
from typing_extensions import Annotated


def not_empty(value:str):
    """空文字の判定."""
    if "" != value:
        raise ValueError(f"{value}は空文字は許容しません")
    return value

NotEmptyStr = Annotated[str, AfterValidator(not_empty)]
"""空文字を許容しないstr型"""
