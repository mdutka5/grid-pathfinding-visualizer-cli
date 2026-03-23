from src.base.grid_pathfinding import GridPathfinding
from src.base.grid_coord import GridCoord
from src.tree.node import Node
from src.tree.tree import Tree
from src.solvers.solver_type import Solver
from collections import deque
import time

class BFS(Solver):
    def __init__(self, problem: GridPathfinding):
        self.problem = problem
        self.root = Node(
            state = self.problem.start,
        )
        self.tree = Tree(self.root)
        self.queue = deque()
        self.visited: set[GridCoord] = set()
        self.search_time = 0.0
        self.checked_nodes = 1
        self.name = "BFS"

    def bfs(self) -> Node | None:
        if self.problem.is_goal(self.root.state):
            return self.root

        self.queue.append(self.root)

        while self.queue:
            node = self.queue.popleft()

            if self.problem.is_goal(node.state):
                return node

            for child in self.tree.expand(self.problem, node):
                self.checked_nodes += 1
                if child.state not in self.visited:
                    self.visited.add(child.state)
                    self.queue.append(child)

        return None

    def solve(self) -> Node | None: 
        start_time = time.perf_counter()
        node = self.bfs()
        end_time = time.perf_counter()
        self.search_time = end_time - start_time
        return node
