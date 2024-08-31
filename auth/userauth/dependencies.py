from user.UserRepository import UserRepository
from auth.userauth.UserService import AuthHandler

userRepo = UserRepository()

auth_handler = AuthHandler(userRepo)

async def returnhandler() -> AuthHandler:
    return auth_handler