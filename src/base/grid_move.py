from enum import Enum

class GridMove(Enum):
    """Enum class representing all moves on grid."""
    N = (-1,0)
    NE = (-1,1)
    E = (0,1)
    SE = (1,1)
    S = (1,0)
    SW = (1,-1)
    W = (0,-1)
    NW = (-1,-1)
    
    @staticmethod
    def _diagonal_moves() -> list[GridMove]:
        return [GridMove.NE, GridMove.SE, GridMove.SW, GridMove.NW]

    def is_diagonal(self) -> bool:
        if self in GridMove._diagonal_moves():
            return True
        return False





