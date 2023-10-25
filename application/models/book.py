"""BookテーブルのORM."""

from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Book(Base):
    """本テーブルのORM."""

    __tablename__ = "book"

    title: Mapped[str] = mapped_column(comment="本の題名")

    def __str__(self):
        """idと名前を設定."""
        return f"Book_{self.id}:{self.title}"
