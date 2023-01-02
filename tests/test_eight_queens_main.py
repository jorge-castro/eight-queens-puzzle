from eight_queens_puzzle.main import Chessboard, solve, is_safe


# Number of solutions to the n-queens problem for boards of size 0-27
number_of_solutions = [
    1,
    1,
    0,
    0,
    2,
    10,
    4,
    40,
    92,
    352,
    724,
    2680,
    14200,
    73712,
    365596,
    2279184,
    14772512,
    95815104,
    666090624,
    4968057848,
    39029188884,
    314666222712,
    2691008701644,
    24233937684440,
    227514171973736,
    2207893435808352,
    22317699616364044,
    234907967154122528,
]


def test_solve():
    # Test solve() with boards of size 1-12; bigger boards can be tested but
    # doing so will take significantly longer
    for size in range(1, 13):
        chessboard = Chessboard(size)
        solution_count = 0

        for i, solution in enumerate(solve(chessboard), start=1):
            solution_count = i

        assert solution_count == number_of_solutions[size]


def test_is_safe():
    chessboard = Chessboard()
    # Place a queen in the first column in the first row
    chessboard[0][0] = True

    # Position in the first column in the second row (vertically aligned) should
    # be deemed unsafe
    assert not is_safe(chessboard, 1, 0)
    # Position in the second column in the second row (diagonally aligned)
    # should be deemed unsafe
    assert not is_safe(chessboard, 1, 1)
    # Position in the third column in the second row should be deemed safe
    assert is_safe(chessboard, 1, 2)
