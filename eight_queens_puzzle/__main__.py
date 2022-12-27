import sys

from .eight_queens_puzzle import Chessboard, solve


size = int(sys.argv[1]) if len(sys.argv) >= 2 else 8
chessboard = Chessboard(size)

for i, solution in enumerate(solve(chessboard), start=1):
    print("*" * 20)
    print(f"Solution number: {i}")
    print(solution)

sys.exit(0)
