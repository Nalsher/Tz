from fastapi import APIRouter, Depends
from database.dbtools import sess_generator
from auth.userauth.dependencies import returnhandler
from schemas.UserSchemas import User
from user.dependencies import service_return


auth_router = APIRouter(prefix="/auth")

@auth_router.post("/login")
async def login_func(model:User,sesion = Depends(sess_generator),service=Depends(returnhandler)):
    login_status = await service.auth_handle(model=model,session=sesion)
    return login_status