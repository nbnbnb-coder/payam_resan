from passlib.context import CryptContext
import hashlib
from jose import jwt
from datetime import datetime,timedelta
import os

SECRET = os.getenv("SECRET_KEY")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(password_hash)

def verify_password(plain_password: str, hashed_password: str):
    password_hash = hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(password_hash, hashed_password)

def create_token(data):
    payload=data.copy()
    payload["exp"]=datetime.utcnow()+timedelta(days=1)
    return jwt.encode(payload,SECRET,"HS256")
