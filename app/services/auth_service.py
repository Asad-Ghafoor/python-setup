
from db.models import User
from db.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from utils.helpers import verify_password, hash_password    
from validations.auth_validation import LoginRequest, RegisterRequest

def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_request.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(login_request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def register(register_request: RegisterRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == register_request.email).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    user = User(email=register_request.email, password=hash_password(register_request.password), username=register_request.username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
