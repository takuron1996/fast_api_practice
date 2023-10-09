"""顧客関連のスキーマ用モジュール."""


from pydantic import BaseModel, Field

from validators import NotEmptyStr


class CustomerModel(BaseModel):
    """顧客モデル."""
    name: NotEmptyStr = Field(
        ...,
        max_length=30,
        min_length=0,
        title="顧客名",
        description="顧客の名前（漢字、全角英語、全角カタカナ、ひらがな）",
        example="Snorlax"
    )
    password: NotEmptyStr = Field(
        ...,
        title="パスワード",
        description="パスワード",
        example="password"
    )


class CustomerResponse(BaseModel):
    """顧客を返却するレスポンス."""
    id: str = Field(
        title="ID",
        description="ID",
        example="01HC7GYK12X4S8J3FHD6K3JV0V"
    )
    name: str = Field(
        title= "顧客名",
        description="顧客名",
        example="Snorlax"
    )
