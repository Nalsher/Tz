from fastapi import Request
from starlette.responses import Response

from auth.jwt.create import create_jwt
from sqlalchemy.ext.asyncio.session import AsyncSession
from user.UserRepository import UserRepository
from schemas.UserSchemas import User


class AuthHandler:
    def __init__(self,userrepo:UserRepository):
        self.repository = userrepo
    async def auth_handle(self,model:User,session:AsyncSession):
        token = await create_jwt(usr_login=model.id)
        try:
            usr = await self.repository.check_login(Session=session,usrname=model.id,
                                              password=model.password)
            resp = Response(content="You successfull loged in")
            resp.set_cookie(key="token",value=token)
            return resp
        except:
            return Response(content="Error no such usr",status_code=403)


