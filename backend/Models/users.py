from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')

#login

class Login(BaseModel):
    username: str
    password: str

#register
class Register(BaseModel):
    username: str
    password: str
    e_mail: str
    phone_number: str | None = Field(default=None)
    name: str
    last_name: str

class ResponseSchemas(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None

class TokenResponse(BaseModel):
    acess_token: str
    token_type: str