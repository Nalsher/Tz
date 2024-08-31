from fastapi import Depends
from starlette.responses import Response

from spellerApi.textApi import json_to_text
from user.UserCrud import UserService
from tasks.TaskRepository import TaskRepository
from sqlalchemy.ext.asyncio.session import AsyncSession
from database.dbschemas import Tasks
from middlewares.check_middleware import middleware,middleware_username

class TaskService:
    def __init__(self,user_repository:UserService,task_repository:TaskRepository):
        self.user_service = user_repository
        self.task_repository = task_repository
    async def task_add(self,text:str,AsyncSessia:AsyncSession,token:str):
        json_text = text.replace(" ","+")
        final_text = await json_to_text(text=json_text)
        valid = await middleware(token)
        if valid:
            username = await middleware_username(token)
            usr = await self.user_service.get_user(session=AsyncSessia,username=username)
            task_id = await self.task_repository.create_task(AsyncSesion=AsyncSessia,text = text,usrname=usr.username)
            return Response(content="Task added successful",status_code=200)
        else:
            return Response(content="You hasnt auth yet",status_code=401)
    async def task_get(self,AsyncSessia:AsyncSession,token:str):
        username = await middleware_username(token)
        usrs = await self.task_repository.get_tasks(AsyncSession=AsyncSessia,username=username)
        return usrs
