from src.base.grid_pathfinding import GridPathfinding
from src.tree.node import Node
from src.tree.tree import Tree
from src.base.grid_coord import GridCoord
from src.solvers.solver_type import Solver
import time

class DFSRecursive(Solver):
    def __init__(self, problem: GridPathfinding):
        self.problem = problem
        self.visited: set[GridCoord] = set()
        self.root = Node(
            prev=None,
            state=problem.start,
            action=None,
            parent=None,
            cost=0
        )
        self.tree = Tree(self.root)
        self.search_time = 0.0
        self.checked_nodes = 1
        self.name = "DFS-recursive"

    def dfs_recursive(self, node: Node) -> Node | None:
        self.checked_nodes += 1
        if self.problem.is_goal(node.state):
            return node
        if node.state in self.visited:
            return None
        
        self.visited.add(node.state)

        for child in self.tree.expand(self.problem, node):
            candidate = self.dfs_recursive(child)

            if candidate is not None:
                return candidate
        
        return None

    def solve(self) -> Node | None:
        start_time = time.perf_counter()
        node = self.dfs_recursive(self.root)
        finish_time = time.perf_counter()
        self.search_time = finish_time - start_time
        return node

