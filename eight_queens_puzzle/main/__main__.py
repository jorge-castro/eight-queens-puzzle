import sys

from .eight_queens_puzzle import Chessboard, solve


size = int(sys.argv[1]) if len(sys.argv) >= 2 and int(sys.argv[1]) >= 1 else 8
chessboard = Chessboard(size)

for i, solution in enumerate(solve(chessboard), start=1):
    print("*" * (len(solution) * 2))
    print(f"Solution #{i}")
    print("*" * (len(solution) * 2))
    print(solution)

sys.exit(0)
