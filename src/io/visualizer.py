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
        NO_VISUAL: bool
    ):
        reversed_solution = Node.reverse_node(solution_node)
        
        if NO_VISUAL:
            if isinstance(solver, BidirectionalSolver):
                original_board = problem.grid.board.copy()
                Visualizer._animation_start(problem, nodes=solver.both_paths, bidir=True)
                problem.grid.board = original_board

            Visualizer._animation_start(problem, reversed_solution)
            print("\n"*problem.grid.shape[0], end='')
    
    @staticmethod
    def _print_to_terminal(frame: str, problem: GridPathfinding) -> None:
            sys.stdout.write(frame)
            sys.stdout.flush()
            sys.stdout.write(f"\033[{problem.grid.shape[0]}A\r")
    
    @staticmethod
    def _animation_start(
            problem: GridPathfinding,
            reversed_solution: Node | None = None, 
            bidir=False, 
            nodes: tuple[Node,Node] | None = None
    ) -> None:
        if not bidir:
            if reversed_solution is None:
                return
            while reversed_solution.prev is not None:
                Visualizer._print_to_terminal(problem.next_frame(reversed_solution), problem)
                reversed_solution = reversed_solution.prev
                time.sleep(0.02)
        else:
            if nodes is None:
                return
            node_l, node_r = nodes
            reversed_l = Node.reverse_node(node_l)
            reversed_r = Node.reverse_node(node_r)
            while reversed_l is not None or reversed_r is not None: 
                Visualizer._print_to_terminal(problem.next_frame_bidir(reversed_l, reversed_r), problem)
                if reversed_l is not None:
                    reversed_l = reversed_l.prev
                if reversed_r is not None:
                    reversed_r = reversed_r.prev
                time.sleep(0.02)
