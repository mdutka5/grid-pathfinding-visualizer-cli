from enum import Enum

class GridCell(Enum):
    """Enum class indicating field in grid in grid pathfinding problem."""
    EMPTY = " "
    WALL = "#"
    START = "S"
    GOAL = "G"

    @staticmethod
    def from_value(val: str) -> GridCell:
        """Returns GridCell object based on corresponding string value."""
        if val == GridCell.EMPTY.value:
            return GridCell.EMPTY
        elif val == GridCell.WALL.value:
            return GridCell.WALL
        elif val == GridCell.START.value:
            return GridCell.START
        elif val == GridCell.GOAL.value:
            return GridCell.GOAL
        else:
            err_message = f"Unidentiefied cell value: '{val}'"
            raise ValueError(err_message)
