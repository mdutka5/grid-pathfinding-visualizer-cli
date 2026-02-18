from typing import Hashable, Union
from dataclasses import dataclass

@dataclass(eq=True)
class GridCoord(Hashable):

    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x,self.y))

    def __add__(self, other: Union[GridCoord, tuple[int,int]]) -> GridCoord:
        shift_x, shift_y = other
        return GridCoord(self.x + shift_x, self.y + shift_y)

    def __iter__(self):
        return iter((self.x,self.y))
