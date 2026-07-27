from models import Board, Card, User


class TestUserModel:
    def test_create_user(self):
        user = User(email="test@example.com", hashed_password="hashed")
        assert user.email == "test@example.com"
        assert user.hashed_password == "hashed"

    def test_user_repr(self):
        user = User(id=1, email="test@example.com", hashed_password="hashed")
        assert user.id == 1


class TestBoardModel:
    def test_create_board(self):
        board = Board(title="My Board", user_id=1)
        assert board.title == "My Board"
        assert board.user_id == 1


class TestCardModel:
    def test_create_card_with_status(self):
        card = Card(title="Task", status="todo", position=0, board_id=1)
        assert card.title == "Task"
        assert card.status == "todo"
        assert card.position == 0
        assert card.description is None

    def test_create_card_full(self):
        card = Card(
            title="Task", description="Details", status="in_progress", position=3, board_id=2
        )
        assert card.title == "Task"
        assert card.description == "Details"
        assert card.status == "in_progress"
        assert card.position == 3
        assert card.board_id == 2
