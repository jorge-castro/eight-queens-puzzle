from __future__ import annotations

from typing import Generator


class Chessboard:
    """A class representing a 2D chessboard. Each board position is represented
    by a bool denoting whether a piece is present or not.
    """

    def __init__(self, size: int = 8):
        """Initialize an n x n chessboard where n = size."""
        self._rows = [[False] * size for _ in range(size)]
        self._size = size

    def __len__(self):
        """Return the number of rows and columns in the board."""
        return self._size

    def __iter__(self):
        """Iterate over the rows in the board."""
        return iter(self._rows)

    def __getitem__(self, key):
        """Return the row(s) at the given index or slice."""
        return self._rows[key]

    def __str__(self):
        """Return a string with a visual representation of the board."""
        return "\n".join(" ".join("x" if _ else "□" for _ in row) for row in self)

    def solve(self, row_index: int = 0) -> Generator[Chessboard, None, None]:
        """Return a generator containing all solutions to the board."""
        row = self[row_index]

        for column_index in range(len(self)):
            if not self.is_safe(row_index, column_index):
                continue
            else:
                if True in row:
                    row[row.index(True)] = False

                row[column_index] = True

                if row_index == len(self) - 1:
                    yield self
                else:
                    yield from self.solve(row_index + 1)

    def is_safe(self, row_index: int, column_index: int) -> bool:
        """Check if queens in previous rows represent a threat to the given position."""
        for i, row in enumerate(self[:row_index]):
            # Check for vertical attack
            if row[column_index] == True:
                return False

            # Check for diagonal attack
            if abs(row_index - i) == abs(column_index - row.index(True)):
                return False

        return True
