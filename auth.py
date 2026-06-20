from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
import os

SECRET = os.getenv("SECRET_KEY")

pwd=CryptContext(schemes=["bcrypt"])

def hash_password(p):
    return pwd.hash(p)

def verify_password(p,h):
    return pwd.verify(p,h)

def create_token(data):
    payload=data.copy()
    payload["exp"]=datetime.utcnow()+timedelta(days=1)
    return jwt.encode(payload,SECRET,"HS256")
