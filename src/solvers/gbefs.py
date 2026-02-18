from src.base.grid_pathfinding import GridPathfinding
from src.tree.node import Node
from src.tree.tree import Tree
from src.utils.priority_queue import PriorityQueue
from typing import Callable
from src.solvers.solver_type import Solver
import time

class GBeFS(Solver):
    def __init__(self, problem: GridPathfinding, heuristic: Callable[[Node], float]):
        self.problem = problem
        self.heuristic = heuristic
        self.root = Node(
            prev = None,
            state = self.problem.start,
            action = None,
            cost = 0.0,
            parent= None
        )
        self.tree = Tree(self.root)
        self.queue = PriorityQueue(self.heuristic)
        self.visited = set()
        self.visited.add(self.root.state)
        self.search_time = 0.0
        self.checked_nodes = 1
        self.name = "Greedy BeFS"

    def gbefs(self) -> Node | None:
        if self.problem.is_goal(self.root.state):
            return self.root

        self.queue.push(self.root)

        while self.queue:
            current_node = self.queue.pop()

            if self.problem.is_goal(current_node.state):
                return current_node

            for child in self.tree.expand(self.problem, current_node):
                self.checked_nodes += 1
                if child.state not in self.visited:
                    self.visited.add(child.state)
                    self.queue.push(child)

        return None

    def solve(self) -> Node | None: 
        start_time = time.perf_counter()
        node = self.gbefs()
        end_time = time.perf_counter()
        self.search_time = end_time - start_time
        return node
