from sqlalchemy import Column, Integer
from sqlalchemy.types import PickleType
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Solution(Base):
    __tablename__ = "solution"

    id = Column(Integer, primary_key=True)
    board_size = Column(Integer)
    number = Column(Integer)
    board = Column(PickleType)

    def __repr__(self):
        return (
            f"Solution(id={self.id!r},"
            f"board_size={self.board_size!r},"
            f"number={self.number!r},"
            f"board={self.board!r})"
        )
