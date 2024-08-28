from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from database.dbschemas import User


class UserRepository:
    async def create_user(self,Session:AsyncSession,usrnme:str) -> User:
        async with Session as sess:
            new_user = User(username=usrnme)
            sess.add(new_user)
            await sess.commit()
            return new_user
