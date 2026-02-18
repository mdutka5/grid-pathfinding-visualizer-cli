from abc import ABC, abstractmethod
from src.tree.node import Node

class Heuristic(ABC):
    name: str
    """Abstract class for all of the Heuristics."""
    @abstractmethod
    def __call__(self, node: Node) -> float:
        pass
