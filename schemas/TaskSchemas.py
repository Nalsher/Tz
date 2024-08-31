from typing import List

from pydantic import BaseModel

class Task(BaseModel):
    text: str

class TaskList(BaseModel):
    tasks: List[Task]