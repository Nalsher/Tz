from auth.jwt.check import check_if_valid
from auth.jwt.get_usrname import get_usrname

async def middleware(token:str | None = None) -> bool:
    if token:
        check = await check_if_valid(token)
        return check
    else:
        return False

async def middleware_username(token:str | None = None) -> str | bool:
    if token:
        username = await get_usrname(token)
        return username
    else:
        return False

###
### Мидлаварь чекаем куки проверяме jwt
### возвращает boolean тру можно делать действия, фолс нет