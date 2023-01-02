import sys

from sqlalchemy import select

from eight_queens_puzzle import Session
from eight_queens_puzzle.models import Solution


size = int(sys.argv[1]) if len(sys.argv) >= 2 and int(sys.argv[1]) >= 1 else 8

with Session() as session:
    solutions = session.execute(
        select(Solution.board_size, Solution.number, Solution.board).where(
            Solution.board_size == size
        )
    ).all()

for solution in solutions:
    print("*" * (solution[0] * 2))
    print(f"Solution #{solution[1]}")
    print("*" * (solution[0] * 2))
    print(solution[2])
