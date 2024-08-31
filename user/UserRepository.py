from typing import List

from certifi import where
from pydantic_core.core_schema import uuid_schema
from sqlalchemy import Select, select, Update
from sqlalchemy.ext.asyncio import AsyncSession

from database.dbschemas import User


class UserRepository:
    async def create_user(self,Session:AsyncSession,usrnme:str,password:str):
        async with Session as sess:
            new_user = User(username=usrnme,password=password)
            sess.add(new_user)
            await sess.commit()
    async def get_user(self,Session:AsyncSession,usrname:str) -> User:
        async with Session as sess:
            user = Select(User).where(User.username == usrname)
            result = await sess.execute(user)
            return result.scalar_one()
    async def get_all_tasks(self,Session:AsyncSession,usrname:str):
        async with Session as sess:
            usr = Select(User.questions).where(User.username==usrname)
            result = await sess.execute(usr)
            return result.scalar_one()
    async def check_login(self,Session:AsyncSession,usrname:str,password:str):
        try:
            async with Session as sess:
                query = Select(User).where(User.username==usrname,User.password==password)
                result = await sess.execute(query)
                return result.scalar_one()
        except:
            raise Exception("NO user")
