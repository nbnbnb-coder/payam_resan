from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from auth import hash_password,verify_password,create_token

router=APIRouter()

def db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(username:str,password:str,db:Session=Depends(db)):
    user=User(username=username,password=hash_password(password))
    db.add(user)
    db.commit()
    return {"status":"ok"}


@router.post("/login")
def login(username:str,password:str,db:Session=Depends(db)):
    user=db.query(User).filter(User.username==username).first()

    if not user:
        return {"error":"user"}

    if not verify_password(password,user.password):
        return {"error":"pass"}

    token=create_token({"user_id":user.id})

    return {"token":token,"id":user.id}


@router.get("/users")
def users(db:Session=Depends(db)):
    users=db.query(User).all()
    return [{"id":u.id,"username":u.username} for u in users]
