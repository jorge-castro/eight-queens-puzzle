import pytest
from sqlalchemy import create_mock_engine

from eight_queens_puzzle.models import Base


@pytest.fixture
def mock_engine():
    def dump(sql, *multiparams, **params):
        print(sql.compile(dialect=engine.dialect))

    engine = create_mock_engine("postgresql://", dump)

    return engine


def test_create_all(mock_engine):
    Base.metadata.create_all(mock_engine)


def test_drop_all(mock_engine):
    Base.metadata.drop_all(mock_engine)
