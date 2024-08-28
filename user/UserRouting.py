from fastapi.routing import APIRouter
from schemas.UserSchemas import User
from user.UserCrud import UserService
from fastapi import Depends
from database.dbtools import sess_generator
from user.dependencies import service_return

users = APIRouter(prefix="/user")

@users.post("/create")
async def UserCreate(model:User,session = Depends(sess_generator),
                     Service = Depends(service_return)):
    user_create = await Service.create_user(usrname=model.id,AsyncSesion=session)
