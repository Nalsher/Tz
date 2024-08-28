import os
from sqlalchemy.ext.asyncio.engine import create_async_engine
from dotenv import load_dotenv

load_dotenv()

namedb = os.environ.get("POSTGRES_DB")
nameusr = os.environ.get("POSTGRES_USER")
namepass = os.environ.get("POSTGRES_PASSWORD")
namehost = os.environ.get("PGHOST")


class Baseconf:
    @property
    def URL(self):
        return f"postgresql+asyncpg://{nameusr}:{namepass}@{namehost}:5432/{namedb}"
Settings = Baseconf()

engine = create_async_engine(url=Settings.URL,echo=True)