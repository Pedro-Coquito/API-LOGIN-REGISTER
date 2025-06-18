from sqlmodel import SQLModel, create_engine, Field, Session, select


DATABASE_URL = "Adicione sua DB aqui"
engine = create_engine(DATABASE_URL, echo=True)


def get_db():
    with Session(engine) as session:
        yield session


#jwt

SECRET_KEY="ProjetoHugo"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30
