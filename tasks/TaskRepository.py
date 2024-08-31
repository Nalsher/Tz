from sqlalchemy import Select
from sqlalchemy.ext.asyncio.session import AsyncSession
from schemas.TaskSchemas import Task, TaskList

from database.dbschemas import Tasks

class TaskRepository:
    async def create_task(self,AsyncSesion:AsyncSession,text:str,usrname:str):
        async with AsyncSesion as sess:
            task = Tasks(text=text,user_id=usrname)
            sess.add(task)
            await sess.flush()
            await sess.refresh(task)
            await sess.commit()
            return task.id
    async def get_tasks(self,AsyncSession:AsyncSession,username:str):
        async with AsyncSession as sess:
            query = Select(Tasks).where(Tasks.user_id==username)
            exec = await sess.execute(query)
            result = exec.scalars()
            dictionary = []
            for i in result:
                dictionary.append({"text":i.text})
            tasks = TaskList(tasks=dictionary)
            return tasks.dict()



