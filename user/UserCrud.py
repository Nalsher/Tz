from user.UserRepository import UserRepository
from sqlalchemy.ext.asyncio.session import AsyncSession
from database.dbschemas import User



class UserService:
    def __init__(self,repository: UserRepository):
        self.rep = repository

    async def create_user(self,password:str,usrname:str,AsyncSesion:AsyncSession):
        result = await self.rep.create_user(usrnme=usrname,password=password,Session=AsyncSesion)

    async def get_user(self,session:AsyncSession,username:str):
        result = await self.rep.get_user(Session=session,usrname=username)
        return result

    async def get_all_tasks(self,session:AsyncSession,username:str):
        result = await self.rep.get_all_tasks(Session=session,usrname=username)
        return result

    async def update_user_tasks(self,user:User,task_id:int,AsyncSessia:AsyncSession):
        result = await self.rep.add_task_user(Session=AsyncSessia,usr=user,task_id=task_id)
        return result