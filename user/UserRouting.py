from fastapi.routing import APIRouter
from schemas.UserSchemas import User
from fastapi import Depends
from database.dbtools import sess_generator
from user.dependencies import service_return

user_router = APIRouter(prefix="/user")

@user_router.post("/create")
async def UserCreate(model:User,session = Depends(sess_generator),
                     Service = Depends(service_return)):
    user_create = await Service.create_user(password=model.password,usrname=model.id,AsyncSesion=session)

