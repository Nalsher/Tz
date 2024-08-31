from database.dbschemas import Base
from database.config import engine
from sqlalchemy.ext.asyncio.session import async_session,async_sessionmaker, AsyncSession

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

sessionmaker = async_sessionmaker(engine,autoflush=True,expire_on_commit=False)

async def sess_generator() -> AsyncSession:
    async with sessionmaker() as sess:
        yield sess