from fastapi import FastAPI
from database.dbtools import drop_table,create_table
from user.UserRouting import users


app = FastAPI()

app.include_router(users)

@app.get("/")
async def start():
    await create_table()