from src.base.grid_pathfinding import GridPathfinding
from src.tree.node import Node
from src.heuristics.heuristic import Heuristic

class ManhatanHeuristic(Heuristic):
    def __init__(self, problem: GridPathfinding):
        self.problem = problem
        self.name = "Manhatan Heuristic"

    def __call__(self, node: Node) -> float:
        x_distance = abs(self.problem.goal.x - node.state.x)
        y_distance = abs(self.problem.goal.y - node.state.y)
        return x_distance + y_distance
