from database import get_db


def test_get_db_yields_and_closes():
    gen = get_db()
    db = next(gen)
    assert db is not None
    gen.close()
