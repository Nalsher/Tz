from typing import List, Optional
from schemas.TaskSchemas import Task
from pydantic import BaseModel

class User(BaseModel):
    id: str
    password: str

class User_List(User):
    tasks: Optional[List[Task]]