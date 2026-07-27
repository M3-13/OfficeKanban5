import pytest
from pydantic import ValidationError
from schemas import (
    BoardCreate,
    BoardResponse,
    CardCreate,
    CardResponse,
    CardUpdate,
    Token,
    UserCreate,
    UserLogin,
    UserResponse,
)


class TestUserCreate:
    def test_valid_user(self):
        user = UserCreate(email="test@example.com", password="password123")
        assert user.email == "test@example.com"
        assert user.password == "password123"

    def test_invalid_email(self):
        with pytest.raises(ValidationError):
            UserCreate(email="not-an-email", password="password123")

    def test_password_too_short(self):
        with pytest.raises(ValidationError):
            UserCreate(email="test@example.com", password="1234567")

    def test_password_min_length(self):
        user = UserCreate(email="test@example.com", password="12345678")
        assert user.password == "12345678"


class TestUserLogin:
    def test_valid(self):
        login = UserLogin(email="test@example.com", password="anypass")
        assert login.email == "test@example.com"

    def test_invalid_email(self):
        with pytest.raises(ValidationError):
            UserLogin(email="bad", password="anypass")


class TestToken:
    def test_default_token_type(self):
        token = Token(access_token="abc123")
        assert token.token_type == "bearer"

    def test_full(self):
        token = Token(access_token="abc123", token_type="bearer")
        assert token.access_token == "abc123"


class TestUserResponse:
    def test_from_attributes(self):
        resp = UserResponse.model_validate({"id": 1, "email": "test@example.com"})
        assert resp.id == 1
        assert resp.email == "test@example.com"


class TestBoardCreate:
    def test_valid(self):
        board = BoardCreate(title="My Board")
        assert board.title == "My Board"

    def test_empty_title(self):
        with pytest.raises(ValidationError):
            BoardCreate(title="")

    def test_title_too_long(self):
        with pytest.raises(ValidationError):
            BoardCreate(title="x" * 201)


class TestBoardResponse:
    def test_from_attributes(self):
        resp = BoardResponse.model_validate({"id": 1, "title": "Board", "user_id": 2})
        assert resp.id == 1
        assert resp.title == "Board"
        assert resp.user_id == 2


class TestCardCreate:
    def test_valid_with_description(self):
        card = CardCreate(title="Task", description="Do something")
        assert card.title == "Task"
        assert card.description == "Do something"

    def test_valid_without_description(self):
        card = CardCreate(title="Task")
        assert card.title == "Task"
        assert card.description is None

    def test_empty_title(self):
        with pytest.raises(ValidationError):
            CardCreate(title="")

    def test_title_too_long(self):
        with pytest.raises(ValidationError):
            CardCreate(title="x" * 501)


class TestCardUpdate:
    def test_partial_update_title_only(self):
        update = CardUpdate(title="New Title")
        assert update.title == "New Title"
        assert update.description is None
        assert update.status is None
        assert update.position is None

    def test_full_update(self):
        update = CardUpdate(title="T", description="D", status="done", position=5)
        assert update.title == "T"
        assert update.status == "done"

    def test_empty_dict(self):
        update = CardUpdate()
        assert update.title is None


class TestCardResponse:
    def test_from_attributes(self):
        resp = CardResponse.model_validate(
            {
                "id": 1,
                "title": "Card",
                "description": None,
                "status": "todo",
                "position": 0,
                "board_id": 3,
            }
        )
        assert resp.id == 1
        assert resp.status == "todo"
        assert resp.board_id == 3
