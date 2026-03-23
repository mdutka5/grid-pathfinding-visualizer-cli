from src.base.grid_coord import GridCoord
from src.base.grid_cell import GridCell
from src.base.grid import Grid
from src.base.grid_move import GridMove
from src.tree.node import Node

from pathlib import Path
import numpy as np


class GridPathfinding():
    """Class representing grid pathfinding problem"""
    def __init__(self, diagonal_weight):
        self.grid: Grid = Grid()
        self.start: GridCoord = GridCoord(0,0)
        self.goal: GridCoord = GridCoord(0,0)
        self.diagonal_weight: float = diagonal_weight

    def parse_grid(self, problem_name: str) -> None:
        """
        Parses problem from txt file.
        Saves goal and start state into 
        self.goal and self.start and
        creates Grid object.

        parameters:
        problem_name: name of the file in problems/ directory.

        returns:
        None
        """
        
        BASE_PATH = Path(__file__).resolve()
        BASE_PATH = BASE_PATH.parent.parent
        FILE_PATH = BASE_PATH / "problems" / problem_name

        with open(FILE_PATH, 'r') as file:
            rows = file.readlines()

        height = len(rows)
        width = max([len(row) for row in rows])
        
        self.grid.board = np.full((height, width), " ", dtype=object)

        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                if cell == GridCell.WALL.value:
                    self.grid[i, j] = GridCell.WALL.value
                elif cell == GridCell.START.value:
                    self.grid[i, j] = GridCell.START.value
                    self.start = GridCoord(i,j)
                elif cell == GridCell.GOAL.value:
                    self.grid[i, j] = GridCell.GOAL.value
                    self.goal = GridCoord(i,j)
                else:
                    self.grid[i, j] = GridCell.EMPTY.value

    def is_legal_move(self, state: GridCoord, move: GridMove) -> bool:
        """Checks if move can be performed from given state."""
        if move.is_diagonal() and self.diagonal_weight == 0.0:
            return False

        new_state = state + move.value

        if new_state.x < 0 or new_state.x >= self.grid.shape[0]:
            return False
        if new_state.y < 0 or new_state.y >= self.grid.shape[1]:
            return False
        
        if self.grid.get_cell(new_state) == GridCell.WALL:
            return False
        
        return True

    def possible_actions(self, state: GridCoord) -> list[GridMove]:
        """Returns list of all legal moves from given state."""
        return [m for m in GridMove if self.is_legal_move(state, m)]

    def take_action(self, state: GridCoord, action: GridMove) -> GridCoord:
        """
        Returns the new state we will
        reach after performing the (action) from the (state).
        """
        return state + action.value

    def action_cost(self, action: GridMove) -> float:
        """Returns cost of the action"""
        if action.is_diagonal():
            return self.diagonal_weight
        return 1.0
        
    def is_goal(self, state: GridCoord) -> bool:
        """Checks whether (state) is goal state."""
        return state == self.goal

    def steps_to_solution(self, goal_node: Node) -> int:
        """Finds out how many steps it took solver to reach solution."""
        steps = 1
        while goal_node.prev is not None and goal_node.prev.state != self.start and goal_node.prev.state != self.goal:
            goal_node = goal_node.prev
            steps += 1
        return steps

    def next_frame(self, node: Node) -> list[str]:
        """Changes cell in grid represented by (node) to next step in path visualisation."""
        if node.prev is not None and node.prev.state != self.start and node.prev.state != self.goal:
            self.grid.board[node.prev.state.x][node.prev.state.y] = 'o'
            node = node.prev
        return self.board_to_list()

    def board_to_list(self) -> list[str]:
        return ["".join(row) + '\n' for row in self.grid.board.tolist()]

    def next_frame_bidir(self, node_l: Node | None, node_r: Node | None) -> list[str]:
        """
        Single step in path visualisation for bidirectional solvers.
        Similar to self.next_frame(node).
        """
        if (
                node_l is not None 
                and node_l.prev is not None 
                and node_l.prev.state != self.start 
                and node_l.prev.state != self.goal
        ):
            self.grid.board[node_l.prev.state.x][node_l.prev.state.y] = 'o'

        if (
                node_r is not None 
                and node_r.prev is not None 
                and node_r.prev.state != self.start 
                and node_r.prev.state != self.goal
        ):
            self.grid.board[node_r.prev.state.x][node_r.prev.state.y] = 'o'

        return self.board_to_list()

    def __str__(self) -> str:
        rows = ["".join(row) + '\n' for row in self.grid.board.tolist()]
        return "".join(rows)

