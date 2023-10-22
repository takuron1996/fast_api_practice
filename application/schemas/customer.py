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

class LoginCustomerModel(BaseModel):
    """ログインAPI用のモデル."""
    id: NotEmptyStr = Field(
        ...,
        title="ID",
        description="ID",
        example="01HCW7AF8YTZEPGC9CFKPFNY5H"
    )
    password: NotEmptyStr = Field(
        ...,
        title="パスワード",
        description="パスワード",
        example="password"
    )

class LoginCustomerRespones(BaseModel):
    """ログインAPI用のレスポンス."""
    access_token: str = Field(
        title="アクセストークン",
        description="アクセストークン",
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwMUhDVzdBRjhZVFpFUEdDOUNGS1BGTlk1SCIsImV4cCI6MTY5Nzk2OTc0OX0.XFlWBi9rYzBAWYVHojGt3EGHwTTpqRxqxLYGqmuL1Pw"
    )
    token_type: str = Field(
        title="トークンタイプ",
        description="トークンタイプ",
        example= "bearer",
        default="bearer"
    )



