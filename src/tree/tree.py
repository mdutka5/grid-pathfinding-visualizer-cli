from src.tree.node import Node
from src.base.grid_pathfinding import GridPathfinding
from typing import Generator

class Tree():
    def __init__(self, root: Node):
        self.root = root

    def expand(self, problem: GridPathfinding, node: Node) -> Generator[Node]:
        for action in problem.possible_actions(node.state):
            child_state = problem.take_action(node.state, action)
            child_node = Node(
                prev=node,
                state=child_state,
                cost=node.cost + problem.action_cost(action),
                action=action
            )

            yield child_node


