from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    password = Column(String)
    avatar = Column(String,nullable=True)
    last_seen = Column(DateTime,default=datetime.utcnow)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer,primary_key=True)
    sender_id = Column(Integer,ForeignKey("users.id"))
    receiver_id = Column(Integer)
    content = Column(String)
    type = Column(String)
    timestamp = Column(DateTime,default=datetime.utcnow)
