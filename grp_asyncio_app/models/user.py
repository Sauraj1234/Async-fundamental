from sqlalchemy import Integer, String, Column, select

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "meta"} 

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)