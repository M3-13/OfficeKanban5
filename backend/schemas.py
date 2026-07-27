from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    email: str

    model_config = {"from_attributes": True}


class BoardCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)


class BoardResponse(BaseModel):
    id: int
    title: str
    user_id: int

    model_config = {"from_attributes": True}


class CardCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=500)
    description: str | None = None


class CardUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=500)
    description: str | None = None
    status: str | None = None
    position: int | None = None


class CardResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    position: int
    board_id: int

    model_config = {"from_attributes": True}
