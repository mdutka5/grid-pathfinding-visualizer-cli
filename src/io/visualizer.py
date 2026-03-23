import sys
import time
from src.base.grid_pathfinding import GridPathfinding
from src.solvers.solver_type import *
from src.tree.node import Node
import blessed
from math import floor

import sys
import time
from src.base.grid_pathfinding import GridPathfinding
from src.solvers.solver_type import *
from src.tree.node import Node


class Visualizer():
    """
    Class responsible for visualizing searching process.
    """
    
    @staticmethod
    def visualize(
        problem: GridPathfinding,
        solver: Solver | BidirectionalSolver,
        solution_node: Node,
        NO_VISUAL: bool,
        SPEED: float
    ):
        reversed_solution = Node.reverse_node(solution_node)
        
        if NO_VISUAL:
            return

        if isinstance(solver, BidirectionalSolver):
            original_board = problem.grid.board.copy()
            Visualizer._animation_start(problem, SPEED, nodes=solver.both_paths, BIDIR=True)
            problem.grid.board = original_board
        else:
            if reversed_solution.state == problem.goal:
                reversed_solution = Node.reverse_node(reversed_solution)

            Visualizer._animation_start(problem, SPEED, reversed_solution)
    
    @staticmethod
    def _roundxy(x, y):
        return int(floor(x)), int(floor(y))

    @staticmethod
    def _colorize_char(char: str, term) -> str:
        if char == '#':
            return term.grey_on_grey('#')
        elif char == 'S':
            return term.gold_on_gold('S')
        elif char == 'G':
            return term.red_on_red('G')
        elif char == 'o':
            return term.green_on_green('o')
        return char
    
    @staticmethod
    def _animation_start(
            problem: GridPathfinding,
            SPEED: float,
            reversed_solution: Node | None = None, 
            BIDIR=False, 
            nodes: tuple[Node,Node] | None = None,
    ) -> None:
        term = blessed.Terminal()

        if not BIDIR:
            if reversed_solution is None:
                return

            with term.hidden_cursor(), term.fullscreen():
                grid_h = problem.grid.shape[0]
                grid_w = problem.grid.shape[1]
                start_y = int((term.height - grid_h) / 2)
                start_x = int((term.width - grid_w) / 2)

                current_y = 0

                while reversed_solution.prev is not None and term.inkey(timeout=1/(SPEED * 10)) != 'q':
                    
                    current_y = start_y
                    for row in problem.next_frame(reversed_solution):
                        row_colored = "".join([Visualizer._colorize_char(c, term) for c in row])

                        print(term.move_xy(start_x, current_y) + row_colored, end='', flush=True)
                        current_y += 1

                    reversed_solution = reversed_solution.prev

                print(term.move_xy(start_x,current_y) + "Path complete. Press any key to exit.")
                term.inkey()
                        
        else:
            if nodes is None:
                return
            node_l, node_r = nodes
            reversed_l = Node.reverse_node(node_l)
            reversed_r = Node.reverse_node(node_r)

            with term.hidden_cursor(), term.fullscreen():
                grid_h = problem.grid.shape[0]
                grid_w = problem.grid.shape[1]
                start_y = int((term.height - grid_h) / 2)
                start_x = int((term.width - grid_w) / 2)

                current_y = 0

                while (reversed_l is not None or reversed_r is not None) and term.inkey(timeout=1/(SPEED * 10)) != 'q':
                    
                    current_y = start_y
                    for row in problem.next_frame_bidir(reversed_l, reversed_r):
                        row_colored = "".join([Visualizer._colorize_char(c, term) for c in row])

                        print(term.move_xy(start_x, current_y) + row_colored, end='', flush=True)
                        current_y += 1

                    if reversed_l is not None:
                        reversed_l = reversed_l.prev
                    if reversed_r is not None:
                        reversed_r = reversed_r.prev

                print(term.move_xy(start_x,current_y) + "Path complete. Press any key to exit.")
                term.inkey()
