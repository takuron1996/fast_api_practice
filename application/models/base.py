"""宣言的マッピング用."""

from datetime import datetime

import ulid
from passlib.context import CryptContext
from sqlalchemy import DateTime, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    """宣言的マッピングの基底クラス."""

    id: Mapped[str] = mapped_column(
        String(26),
        primary_key=True,
        default=lambda: ulid.new().str,
        comment="ID",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PasswordMixin:
    """ハッシュ化したパスワードを設定する用のMixin."""

    _password: Mapped[str] = mapped_column("password", String(60))

    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def set_password(self, password):
        """パスワードをハッシュ化して設定."""
        self._password = PasswordMixin._pwd_context.hash(password)

    def check_password(self, password):
        """設定したパスワードと一致するかどうかを検証."""
        return PasswordMixin._pwd_context.verify(password, self._password)
