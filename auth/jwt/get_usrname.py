import jwt
from auth.jwt.create import secret_key

async def get_usrname(token:str) -> bool:
    try:
        token = jwt.decode(token,key=secret_key,algorithms=["HS256"])
    except:
        return False
    finally:
        data = token.get("login")
        return data