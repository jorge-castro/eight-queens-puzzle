from sqlalchemy import create_mock_engine

from eight_queens_puzzle.models import Base


def test_create_all():
    def dump(sql, *multiparams, **params):
        print(sql.compile(dialect=engine.dialect))

    engine = create_mock_engine("postgresql://", dump)
    Base.metadata.create_all(engine)


def test_drop_all():
    def dump(sql, *multiparams, **params):
        print(sql.compile(dialect=engine.dialect))

    engine = create_mock_engine("postgresql://", dump)
    Base.metadata.drop_all(engine)
