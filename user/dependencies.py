from user.UserRepository import UserRepository
from user.UserCrud import UserService

repo = UserRepository()

service = UserService(repository=repo)

async def service_return():
    return service