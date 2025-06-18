from sqlmodel import Field, SQLModel, create_engine, select, Session
from sqlalchemy import Column, DateTime, func
from backend.Config import engine, get_db
from datetime import datetime 



class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    e_mail: str
    phone_number: str | None = Field(default=None)
    name: str
    last_name: str

create_date: datetime = Field(
    sa_column=Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        )
)

update_date: datetime = Field(
   sa_column=Column(
       DateTime(timezone=True),
       server_default=func.now(),
       onupdate=func.now(),
       nullable=False,
   )
)

