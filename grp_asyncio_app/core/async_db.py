
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = 'postgresql+asyncpg://postgres:12345@localhost:5432/green_db'


engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,          
    max_overflow=20,        
    pool_timeout=30,        
    pool_recycle=1800,      
    pool_pre_ping=True,     
    pool_use_lifo=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base  = declarative_base()

async def init_db():
    """Create tables (runs DDL)."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



