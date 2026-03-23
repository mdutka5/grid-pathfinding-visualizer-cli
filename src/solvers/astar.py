import time
from src.base.grid_pathfinding import GridPathfinding
from src.tree.node import Node
from src.tree.tree import Tree
from src.utils.priority_queue import PriorityQueue
from typing import Callable
from src.solvers.solver_type import Solver

class AStar(Solver):
    def __init__(self, problem: GridPathfinding, heuristic: Callable[[Node], float]):
        self.problem = problem
        self.heuristic = heuristic
        self.root = Node(
            state = self.problem.start,
        )
        self.tree = Tree(self.root)
        self.queue = PriorityQueue(lambda x: x.cost + self.heuristic(x))
        self.visited = {self.root.state: 0.0}
        self.search_time = 0.0
        self.checked_nodes = 1
        self.name = "A-star"

    def astar(self) -> Node | None:
        self.queue.push(self.root)

        while self.queue:
            current_node = self.queue.pop()

            if self.problem.is_goal(current_node.state):
                return current_node

            for child in self.tree.expand(self.problem, current_node):
                self.checked_nodes += 1
                if child.state not in self.visited or child.cost < self.visited[child.state]:
                    self.queue.push(child)
                    self.visited[child.state] = child.cost

        return None


    def solve(self) -> Node | None: 
        start_time = time.perf_counter()
        node = self.astar()
        end_time = time.perf_counter()
        self.search_time = end_time - start_time
        return node
