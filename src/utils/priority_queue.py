from src.tree.node import Node
from dataclasses import dataclass, field
from typing import Callable
import heapq

@dataclass(order=True)
class PQitem():
    value: float
    node: Node = field(compare=False)

class PriorityQueue():
    def __init__(self, compare_function: Callable[[Node], float]):
        self.fun = compare_function
        self.heap: list[PQitem] = []
    
    def push(self, node: Node) -> None:
        heapq.heappush(self.heap, PQitem(self.fun(node), node))

    def pop(self) -> Node:
        hitem = heapq.heappop(self.heap)
        return hitem.node

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def __bool__(self):
        return not self.is_empty()

