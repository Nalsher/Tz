from fastapi import FastAPI
from database.dbtools import drop_table,create_table
from user.UserRouting import user_router
from auth.userauth.AuthRouting import auth_router
from tasks.TaskRouting import tasks_router


app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(tasks_router)

@app.get("/")
async def start():
    await drop_table()
    await create_table()