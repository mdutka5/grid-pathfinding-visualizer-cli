from src.base.grid_coord import GridCoord
from src.base.grid_move import GridMove

class Node():
    def __init__(
        self,
        state: GridCoord,
        prev: Node | None = None,
        action: GridMove | None = None,
        cost: float = 0.0,
    ):
        self.state = state
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
    def reverse_node(node: Node) -> Node:
        pre = None
        curr = node
        next = None

        while curr is not None:
            next = curr.prev
            curr.prev = pre
            pre = curr
            curr = next
        if pre is None:
            raise ValueError("./src/tree/node.py -> reverse_node -> pre is None.")
        return pre
