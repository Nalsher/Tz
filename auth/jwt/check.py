import jwt
import datetime
from auth.jwt.create import secret_key


async def check_if_valid(token:str) -> bool:
    try:
        token = jwt.decode(token,key=secret_key,algorithms=["HS256"])
    except:
        return False
    finally:
        data = token.get("exp_time")
        date = datetime.datetime.strptime(data,"%Y-%m-%d %H:%M:%S.%f")
        if datetime.datetime.now() - date > datetime.timedelta(minutes=59):
            return False
        else:
            return True
