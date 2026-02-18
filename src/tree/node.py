from src.base.grid_coord import GridCoord
from src.base.grid_move import GridMove

class Node():
    def __init__(
        self,
        state: GridCoord,
        prev: Node | None,
        parent: GridCoord | None,
        action: GridMove | None,
        cost: float,
    ):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.state}"

    def __repr__(self) -> str:
        return f"{self.state}"

    def __hash__(self):
        return hash(self.state)
    
    @staticmethod
    def reverse_node(node: Node) -> Node | None:
        pre = None
        curr = node
        next = None

        while curr is not None:
            next = curr.prev
            curr.prev = pre
            pre = curr
            curr = next

        if pre is None:
            raise ValueError("Pre is None!")

        if pre is not None:
            return pre
