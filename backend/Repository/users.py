from typing import TypeVar, Optional, Generic
from sqlmodel import Session, select
from datetime import datetime, timedelta

from jose import JWTError, jwt
from backend.Config import SECRET_KEY, ALGORITHM

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPBasicCredentials

T = TypeVar('T')

#users

class BaseRepo():

    @staticmethod
    def insert(db: Session, model: Generic[T]):
        db.add(model)
        db.commit()
        db.refresh(model)

class UserRepo(BaseRepo):
    @staticmethod
    def find_by_username(db: Session, model: Generic[T], username:str):

        statement = select(model).where(model.username == username)
        return db.exec(statement).first()

    
class JWTRepo():
    def generate_token(data: dict, expires_delta: Optional[timedelta]= None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes= 15)
            to_encode.update({"exp": expire})
            encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
            return encode_jwt
        
    def decode_token(token: str):
        try:
            decode_token = jwt.decode(token,SECRET_KEY, algorithms= ALGORITHM)
            return decode_token if decode_token('expires') >= datetime.time() else None
        except:
            return{}

