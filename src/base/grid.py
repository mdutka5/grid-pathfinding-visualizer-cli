from numpy.typing import NDArray
from typing import cast

from src.base.grid_cell import GridCell
from src.base.grid_coord import GridCoord

class Grid():
    """Class representing grid in grid pathfinding problem implemented using numpy array."""
    def __init__(self):
        self.board: NDArray

    @property
    def shape(self) -> tuple[int, int]:
        return cast(tuple[int,int], self.board.shape)

    def __getitem__(self, pos):
        x, y = pos
        return self.board[x, y]

    def __setitem__(self, pos, item):
        x, y = pos
        self.board[x, y] = item

    def get_cell(self, coord: GridCoord) -> GridCell:
        cell = self.board[coord.x][coord.y]
        return GridCell.from_value(cell)
