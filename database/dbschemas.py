from typing import List

from sqlalchemy import Table, MetaData, String, ForeignKey, Integer, Column, ARRAY
from sqlalchemy.orm import mapped_column, declarative_base, DeclarativeBase, Mapped, relationship, Relationship


class Base(DeclarativeBase):
    pass

metadata = MetaData()

Base.metadata = metadata

class User(Base):
    __tablename__ = "user"
    username=Column("username",String,primary_key=True)
    password=Column("password",String)

class Tasks(Base):
    __tablename__ = "tasks"
    id=Column("id",Integer,primary_key=True)
    text=Column("text",String,nullable=False)
    user_id=Column("fk",String,ForeignKey("user.username"))


