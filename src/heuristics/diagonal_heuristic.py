from src.base.grid_pathfinding import GridPathfinding
from src.tree.node import Node
from src.heuristics.heuristic import Heuristic

class DiagonalHeuristic(Heuristic):
    def __init__(self, problem: GridPathfinding):
        self.problem = problem
        self.name = "Diagonal Heuristic"

    def __call__(self, node: Node) -> float:
        x_goal = self.problem.goal.x
        y_goal = self.problem.goal.y
        x = abs(node.state.x - x_goal) 
        y = abs(node.state.y - y_goal) 

        diagonal = min(x, y)
        straight = abs(x - y)
        return self.problem.diagonal_weight * diagonal + straight
