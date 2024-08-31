from sqlalchemy.sql.annotation import Annotated

from tasks.dependencies import task_return
from fastapi import APIRouter,Depends
from database.dbtools import sess_generator
from schemas.TaskSchemas import Task
from fastapi import Cookie
from typing import Annotated

from user.dependencies import service

tasks_router = APIRouter(prefix="/tasks")

@tasks_router.post("/create")
async def task_create(model:Task,token:Annotated[str | None , Cookie()] = None,session = Depends(sess_generator),
                      Service = Depends(task_return)):
    task = await Service.task_add(text=model.text,AsyncSessia=session,token=token)
    return task

@tasks_router.get("/list")
async def task_check(token:Annotated[str | None , Cookie()] = None,session = Depends(sess_generator),
                     Service = Depends(task_return)):
    task = await Service.task_get(AsyncSessia=session,token=token)
    return task
