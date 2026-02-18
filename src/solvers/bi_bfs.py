from src.base.grid_pathfinding import GridPathfinding
from src.base.grid_coord import GridCoord
from src.tree.node import Node
from src.tree.tree import Tree
from src.solvers.solver_type import BidirectionalSolver
from collections import deque
import time

class BidirectionalBFS(BidirectionalSolver):
    def __init__(self, problem: GridPathfinding):
        self.problem = problem
        self.root_from_start: Node = Node(
            parent=None,
            prev=None,
            state=self.problem.start,
            cost=0.0,
            action=None
        )
        self.root_from_goal: Node = Node(
            parent=None,
            prev=None,
            state=self.problem.goal,
            cost=0.0,
            action=None
        )
        self.tree_from_start: Tree = Tree(
            self.root_from_start
        )
        self.tree_from_goal: Tree = Tree(
            self.root_from_goal
        )
        self.tree: Tree = Tree(
            self.root_from_start
        )
        self.visited_from_start: dict[GridCoord, Node] = {
            self.root_from_start.state: self.root_from_start
        }
        self.visited_from_goal: dict[GridCoord, Node] = {
            self.root_from_goal.state: self.root_from_goal
        }
        self.queue_from_start = deque()
        self.queue_from_goal = deque()
        self.queue_from_start.append(self.root_from_start)
        self.queue_from_goal.append(self.root_from_goal)

        self.both_paths: tuple[Node,Node]
        self.search_time = 0.0
        self.checked_nodes = 1
        self.name = "Bidirectional BFS"
    
    def bi_bfs(self) -> Node | None:
        while self.queue_from_goal and self.queue_from_start:
            if len(self.queue_from_start) <= len(self.queue_from_goal):
                found_node = self._expand_side(
                    self.queue_from_start,
                    self.visited_from_start,
                    self.visited_from_goal
                )
            else:
                found_node = self._expand_side(
                    self.queue_from_goal,
                    self.visited_from_goal,
                    self.visited_from_start,
                )
            if found_node:
                self.both_paths = found_node
                return self._join_paths(found_node)
        
        return None

    def _expand_side(
            self, 
            my_queue: deque, 
            my_visited: dict[GridCoord, Node], 
            other_visited: dict[GridCoord, Node]
    ) -> tuple[Node, Node] | None:
        
        current_node = my_queue.popleft()

        for child in self.tree.expand(self.problem, current_node):
            if child.state in other_visited:
                return (child, other_visited[child.state])
            
            if child.state not in my_visited:
                self.checked_nodes += 1
                my_visited[child.state] = child
                my_queue.append(child)

        return None
    
    def solve(self) -> Node | None:
        start_time = time.perf_counter()
        node = self.bi_bfs()
        end_time = time.perf_counter()
        self.search_time = end_time - start_time
        return node
    
    def _join_paths(self, paths: tuple[Node,Node]) -> Node | None:
        path_states = []
        curr = paths[0]
        while curr:
            path_states.append(curr.state)
            curr = curr.prev
        path_states.reverse() 

        curr = paths[1].prev
        while curr:
            path_states.append(curr.state)
            curr = curr.prev
        new_node = None
        for state in path_states:
            new_node = Node(
                state=state,
                prev=new_node, 
                cost=0.0,
                action=None,
                parent=None
            )
        return Node.reverse_node(new_node) if new_node is not None else None


