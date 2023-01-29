import sys

from .chessboard import Chessboard


size = int(sys.argv[1]) if len(sys.argv) >= 2 and int(sys.argv[1]) >= 1 else 8
chessboard = Chessboard(size)

for i, solution in enumerate(chessboard.solve(), start=1):
    print("*" * (len(solution) * 2))
    print(f"Solution #{i}")
    print("*" * (len(solution) * 2))
    print(solution)

sys.exit(0)
