from tasks.TaskCrud import TaskService
from tasks.TaskRepository import TaskRepository
from user.dependencies import service

task_repo = TaskRepository()

task_service = TaskService(user_repository=service,task_repository=task_repo)

async def task_return() -> TaskService:
    return task_service