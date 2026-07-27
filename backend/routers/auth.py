from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register():
    return {"message": "Not implemented"}


@router.post("/login")
def login():
    return {"message": "Not implemented"}
