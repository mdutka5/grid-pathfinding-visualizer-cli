from abc import ABC, abstractmethod
from src.tree.node import Node
from src.heuristics.heuristic import Heuristic

class Solver(ABC):
    # @property
    # @abstractmethod 
    # def name(self) -> str:
    #     pass
    #
    # @property
    # @abstractmethod 
    # def search_time(self) -> float:
    #     pass
    #
    # @property
    # @abstractmethod 
    # def checked_nodes(self) -> int:
    #     pass
    #
    
    name: str
    checked_nodes: int
    search_time: float
    heuristic: Heuristic | None = None

    @abstractmethod
    def solve(self) -> Node | None:
        pass

class BidirectionalSolver(ABC):
    # @property
    # @abstractmethod 
    # def name(self) -> str:
    #     pass
    #
    # @property
    # @abstractmethod 
    # def search_time(self) -> float:
    #     pass
    #
    # @property
    # @abstractmethod 
    # def checked_nodes(self) -> int:
    #     pass
    #
    # @property
    # @abstractmethod 
    # def both_paths(self) -> tuple[Node, Node]:
    #     pass
    
    name: str
    checked_nodes: int
    search_time: float
    both_paths: tuple[Node, Node]
    heuristic: Heuristic | None = None

    @abstractmethod
    def solve(self) -> Node | None:
        pass
