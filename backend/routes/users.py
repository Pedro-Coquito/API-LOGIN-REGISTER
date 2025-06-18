from fastapi import APIRouter, Depends, status, HTTPException
from backend.Models.users import ResponseSchemas, TokenResponse, Register, Login
from sqlmodel import Session
from backend.Config import get_db
from passlib.context import CryptContext
from backend.Repository.users import UserRepo, JWTRepo
from backend.Tables.db import User

from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(
    tags={"Authentication"}
)

pwd_context = CryptContext(schemes=['bcrypt'] ,deprecated="auto")

security = HTTPBearer()

@router.get("/protected-endpoint")
async def protected_endpoint(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    payload = JWTRepo.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    return {"username": payload.get("sub")}

#register

@router.post('/Register')
async def signup(request: Register, db: Session = Depends(get_db)):
    try: 
        _user = User(
        username= request.username,
        password= pwd_context.hash(request.password),
        e_mail= request.e_mail,
        phone_number= request.phone_number,
        name= request.name,
        last_name= request.last_name)

        print("Usuario a ser salvo no banco de dados:", _user)
        UserRepo.insert(db, _user)
        print("Usuario salvo com sucesso")
        return ResponseSchemas(code="200", status="ok", message="Dados salvos com sucesso")
    except Exception as error :
        
        print(error.args)
        return ResponseSchemas(code="500", status="Error", message="Internal Server Error")

#login
@router.post(
     "/login",
     response_model=ResponseSchemas,
     status_code= status.HTTP_200_OK,
 )

async def login(request: Login, db: Session = Depends(get_db)):
    try: 
        _user = UserRepo.find_by_username(db, User, request.username)

        if not _user:
            return ResponseSchemas(code="401", status="Unauthorized", message="Usuário ou senha inválidos")
        if not pwd_context.verify(request.password, _user.password):
            return ResponseSchemas(code="401", status="Unauthorized", message="Usuário ou senha inválidos")
    
        token = JWTRepo.generate_token({'sub': _user.username})
        return ResponseSchemas(code="200", status="ok", message="Login Valido", result=TokenResponse(acess_token=token, token_type='bearer'))
    
    except Exception as error:
          raise HTTPException (
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Internal Server Error"
        )