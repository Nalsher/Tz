from user.UserRepository import UserRepository
from sqlalchemy.ext.asyncio.session import AsyncSession

class UserService:
    def __init__(self,repository: UserRepository):
        self.rep = repository

    async def create_user(self,usrname:str,AsyncSesion:AsyncSession):
        result = await self.rep.create_user(usrnme=usrname,Session=AsyncSesion)
