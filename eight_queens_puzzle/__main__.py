import sys
from copy import deepcopy

from .main import Chessboard
from .models import Solution
from . import Session, create_tables


create_tables()

with Session.begin() as session:
    size = int(sys.argv[1]) if len(sys.argv) >= 2 and int(sys.argv[1]) >= 1 else 8
    chessboard = Chessboard(size)

    for i, solution in enumerate(chessboard.solve(), start=1):
        session.add(
            Solution(board_size=len(solution), number=i, board=deepcopy(solution))
        )

sys.exit(0)
