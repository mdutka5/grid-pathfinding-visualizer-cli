from src.base.grid_pathfinding import GridPathfinding
from src.tree.node import Node
from src.solvers.solver_type import *


class Reporter():
    """
    Class responsible for:
        - printing messages to user.
        - printing statistics of solution.
        - printing info about state of solver.
    """

    @staticmethod
    def print_problem_info(problem: GridPathfinding, CONCISE: bool):
        if not CONCISE:
            print(f"initial state at: ({problem.start.x}, {problem.start.y})")
            print(f"goal state at: ({problem.goal.x}, {problem.goal.y})")

    @staticmethod
    def print_solution_stats(
            problem: GridPathfinding,
            solver: Solver | BidirectionalSolver,
            solution_node: Node,
            CONCISE: bool
    ):
        if not CONCISE:
            print(f"Solver found solution at: ({solution_node.state.x}, {solution_node.state.y})")
            print(f"Solution is {problem.steps_to_solution(solution_node)} steps long.")
            print(f"It took {round(solver.search_time * 1000, 6)} ms. to find this solution.")
            print(f"Solver({solver.name}) checked {solver.checked_nodes} nodes.")
        else:
            if solver.heuristic is not None:
                print(f"Solver({solver.name}, {solver.heuristic.name}):")
            else:
                print(f"Solver({solver.name}):")
            print(f"{problem.steps_to_solution(solution_node)} steps long.")
            print(f"{round(solver.search_time * 1000, 6)} ms.")
            print(f"{solver.checked_nodes} nodes checked.")
