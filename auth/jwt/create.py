import jwt
import datetime

secret_key = "secret"

async def create_jwt(usr_login: str) -> str:
    payload = {"login": usr_login, "exp_time": str(datetime.datetime.now() + datetime.timedelta(hours=1))}
    token = jwt.encode(payload=payload, key=secret_key)
    return token

