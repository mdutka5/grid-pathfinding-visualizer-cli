from argparse import ArgumentParser, Namespace
from pathlib import Path
import sys

from src.base.grid_pathfinding import GridPathfinding

from src.heuristics.heuristic import Heuristic
from src.heuristics.diagonal_heuristic import DiagonalHeuristic
from src.heuristics.manhatan_heuristic import ManhatanHeuristic
from src.heuristics.euclidean_heuristic import EuclideanHeuristic

from src.solvers.astar import AStar
from src.solvers.bfs import BFS
from src.solvers.bi_bfs import BidirectionalBFS
from src.solvers.dfs_recursive import DFSRecursive
from src.solvers.gbefs import GBeFS
from src.solvers.solver_type import *

class Parser():
    """
    Wrapper class for argparse.ArgumentParser class.
    Used for handling user input.
    """
    def __init__(self):
        self._parser = ArgumentParser(
            description="Grid Pathfinder Visualizer - showcase of popular state-space search algorithms",
            usage="""uv run main.py [SEARCH OPTIONS] [DISPLAY OPTIONS] [PATH TO PROBLEM INSTANCE]
                Search Options:
                -a, --algorithm      {bfs, dfs, bibfs, gbefs, astar}
                -e, --heuristic      {man, euclid, diag}
                -w, --weight         FLOAT (Default: 0 - no diagonal movement)

                Display Options:
                -nv, --no-visual     Disable animation
                -s, --speed          FLOAT (Default: 8)
                -c, --concise        Show summary in condensed way

                Path to problem instance:
                -problems are stored in problems/ directory.
                
                Example usage:
                  uv run main.py -a astar -e man -c problems/plus_grid.txt
                """        
        )
        self._setup_arguments()

    def _setup_arguments(self) -> None:
        """Sets up all arguments used by parser"""

        self._parser.add_argument(
            "problem_file_name",
            help="problems are stored in problems/ directory. Pick one!"
        )

        self._parser.add_argument(
            "-a",
            "--algorithm",
            help="algorithm used to find solution for given problem.",
            type=str
        )

        self._parser.add_argument(
            "-e",
            "--heuristic",
            help="type of heuristic used with algorithm.",
            type=str
        )

        self._parser.add_argument(
            "-w",
            "--weight",
            help="weight of diagonal movement in the grid. Default is 0(no diagonal movement).",
            type=float
        )

        self._parser.add_argument(
            "-nv",
            "--no-visual",
            help="if used animation of solution to the problem wont be shown.",
            action="store_true"
        )

        self._parser.add_argument(
            "-c",
            "--concise",
            help="display performance metrics in condensed summary.",
            action="store_true"
        )

        self._parser.add_argument(
            "-s",
            "--speed",
            help="speed of animation. Default is 8.",
            type=float
        )

    def parse(self) -> tuple[
        GridPathfinding,
        Solver | BidirectionalSolver,
        bool,
        bool,
        float
    ]:
        """Returns parsed arguments from input"""
        args = self._parser.parse_args()
        NO_VISUAL = self._parse_visual(args)
        CONCISE = self._parse_concise(args)
        path_to_problem = self._parse_path(args)
        diagonal_weight = self._parse_weight(args)
        SPEED = self._parse_speed(args)
        problem = self._parse_problem(
            path_to_problem,
            diagonal_weight
        )
        heuristic = self._parse_heuristic(args, problem)
        solver = self._parse_algorithm(args, problem, heuristic)

        return (problem, solver, NO_VISUAL, CONCISE, SPEED)

    def _parse_visual(self, args: Namespace) -> bool:
        return args.no_visual

    def _parse_concise(self, args: Namespace) -> bool:
        return args.concise
    
    def _parse_path(self, args: Namespace) -> str:
        path_to_problem = Path(args.problem_file_name).resolve()
        if not path_to_problem.exists():
            print(f"PATH: {path_to_problem} DOES NOT EXIST.")
            sys.exit(1)
        return str(path_to_problem)
    
    def _parse_weight(self, args: Namespace) -> float:
        return 0 if args.weight is None else args.weight

    def _parse_speed(self, args: Namespace) -> float:
        return 8 if args.speed is None else args.speed
    
    def _parse_problem(self, path: str, diagonal_weight: float) -> GridPathfinding:
        problem = GridPathfinding(diagonal_weight)
        problem.parse_grid(path)
        return problem
    
    def _parse_heuristic(self, args: Namespace, problem: GridPathfinding) -> Heuristic | None:
        if args.heuristic is None:
            return None
        match args.heuristic.lower():
            case "euclid":
                return EuclideanHeuristic(problem)
            case "man":
                return ManhatanHeuristic(problem)
            case "diag":
                return DiagonalHeuristic(problem)
            case _:
                print("PLEASE CHOOSE CORRECT HEURISTIC.")
                sys.exit(5)

    def _parse_algorithm(
            self,
            args: Namespace, 
            problem: GridPathfinding, 
            heuristic: Heuristic | None
    ) -> Solver | BidirectionalSolver:
        match args.algorithm.lower():
            case "dfs":
                return DFSRecursive(problem)
            case "bfs":
                return BFS(problem)
            case "gbefs":
                if heuristic is None:
                    print("THIS ALGORITHM REQUIRES HEURISTIC")
                    sys.exit(6)
                return GBeFS(problem, heuristic)
            case "astar":
                if heuristic is None:
                    print("THIS ALGORITHM REQUIRES HEURISTIC")
                    sys.exit(6)
                return AStar(problem, heuristic)
            case "bibfs":
                return BidirectionalBFS(problem)
            case _:
                print("PLEASE CHOOSE CORRECT ALGORITHM.")
                sys.exit(3)
    
