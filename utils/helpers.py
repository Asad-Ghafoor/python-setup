from logger.logger import logger
from jose import jwt
from config.settings import settings
import bcrypt

def verify_token(token: str):
    return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])

def generate_token(payload: dict):
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)

def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password: str, hashed_password: bytes):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)