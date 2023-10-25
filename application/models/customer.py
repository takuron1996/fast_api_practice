"""CustomerテーブルのORM."""

from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base, PasswordMixin


class Customer(Base, PasswordMixin):
    """顧客テーブルのORM."""

    __tablename__ = "customer"

    name: Mapped[str] = mapped_column(comment="顧客の名前")

    def __str__(self):
        """idと名前を設定."""
        return f"Customer_{self.id}:{self.name}"
