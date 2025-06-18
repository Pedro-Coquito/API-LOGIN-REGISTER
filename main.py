from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import SQLModel, Session, select, Field, create_engine
from contextlib import asynccontextmanager


from backend.Tables.db import engine, User
from backend.Config import get_db
import backend.routes.users as user_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield
    engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(user_routes.router)

