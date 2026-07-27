import os
from contextlib import asynccontextmanager

from database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, boards

FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")


@asynccontextmanager
async def lifespan(application: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="OfficeKanban5", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(boards.router)


@app.get("/health")
def health():
    return {"status": "ok"}
