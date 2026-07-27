import pytest
from auth import create_access_token, get_current_user, get_password_hash, verify_password
from config import JWT_ALGORITHM
from database import Base, get_db
from fastapi import HTTPException
from jose import jwt
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def test_db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = testing_session_local()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def override_get_db(test_db, monkeypatch):
    def _get_db_override():
        yield test_db

    from main import app

    app.dependency_overrides[get_db] = _get_db_override
    yield
    app.dependency_overrides.clear()


def test_create_access_token_content():
    token = create_access_token({"sub": "test@example.com"})
    assert isinstance(token, str)
    assert len(token) > 10


def test_password_hash_and_verify():
    password = "securepassword123"
    hashed = get_password_hash(password)
    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("wrongpassword", hashed) is False


def test_get_current_user_valid(test_db):
    user = User(email="valid@example.com", hashed_password="hashed")
    test_db.add(user)
    test_db.commit()

    token = create_access_token({"sub": "valid@example.com"})
    result = get_current_user(token=token, db=test_db)
    assert result.email == "valid@example.com"


def test_get_current_user_invalid_token(test_db):
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token="invalid.token.here", db=test_db)
    assert exc_info.value.status_code == 401


def test_get_current_user_unknown_user(test_db):
    token = create_access_token({"sub": "ghost@example.com"})
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token=token, db=test_db)
    assert exc_info.value.status_code == 401


def test_get_current_user_missing_sub(test_db):
    from datetime import UTC, datetime, timedelta

    import config

    token = jwt.encode(
        {"exp": datetime.now(UTC) + timedelta(minutes=5)},
        config.JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token=token, db=test_db)
    assert exc_info.value.status_code == 401


def test_get_current_user_expired_token(test_db):
    from datetime import UTC, datetime, timedelta

    import config

    token = jwt.encode(
        {"sub": "user@example.com", "exp": datetime.now(UTC) - timedelta(minutes=5)},
        config.JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )
    with pytest.raises(HTTPException) as exc_info:
        get_current_user(token=token, db=test_db)
    assert exc_info.value.status_code == 401
