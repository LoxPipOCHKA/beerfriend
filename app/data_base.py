from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)
from sqlalchemy.orm import DeclarativeBase

DB_HOST = 'localhost'
DB_PORT = 8000
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_NAME = 'postgres'

DATABASE_URL = f'postgres+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(DATABASE_URL)

async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass