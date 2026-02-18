import math 
from src.base.grid_pathfinding import GridPathfinding
from src.tree.node import Node
from src.heuristics.heuristic import Heuristic

class EuclideanHeuristic(Heuristic):
    def __init__(self, problem: GridPathfinding):
        self.problem = problem
        self.name = "Euclidean Heuristic"

    def __call__(self, node: Node) -> float:
        x_goal = self.problem.goal.x
        y_goal = self.problem.goal.y
        x = (node.state.x - x_goal) 
        y = (node.state.y - y_goal) 
        return math.sqrt(x**2 + y**2)
