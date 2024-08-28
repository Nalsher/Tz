from typing import List

from sqlalchemy import Table, MetaData, String, ForeignKey, Integer
from sqlalchemy.orm import mapped_column, declarative_base, DeclarativeBase, Mapped, relationship


class Base(DeclarativeBase):
    pass

metadata = MetaData()

Base.metadata = metadata

class User(Base):
    __tablename__ = "user"
    username: Mapped[str] = mapped_column(String,primary_key=True)
    questions: Mapped[List] = mapped_column(ForeignKey("tasks.id"),nullable=True)

class Tasks(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    text: Mapped[str] = mapped_column(String,nullable=False)



