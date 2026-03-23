from abc import ABC, abstractmethod
from src.tree.node import Node
from src.heuristics.heuristic import Heuristic

class Solver(ABC):
    name: str
    checked_nodes: int
    search_time: float
    heuristic: Heuristic | None = None

    @abstractmethod
    def solve(self) -> Node | None:
        pass

class BidirectionalSolver(ABC):
    name: str
    checked_nodes: int
    search_time: float
    both_paths: tuple[Node, Node]
    heuristic: Heuristic | None = None

    @abstractmethod
    def solve(self) -> Node | None:
        pass
