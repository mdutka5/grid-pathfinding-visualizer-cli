from numpy.typing import NDArray
from typing import cast

from src.base.grid_cell import GridCell
from src.base.grid_coord import GridCoord

class Grid():
    def __init__(self):
        self.board: NDArray

    @property
    def shape(self) -> tuple[int, int]:
        return cast(tuple[int,int], self.board.shape)

    def __getitem__(self, pos):
        x, y = pos
        return self.board[x, y]

    def get_cell(self, coord: GridCoord) -> GridCell:
        cell = self.board[coord.x][coord.y]
        return GridCell.from_value(cell)
