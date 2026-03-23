from src.io.parser import Parser
from src.io.reporter import Reporter
from src.io.visualizer import Visualizer

def main():
    parser = Parser()
    problem, solver, NO_VISUAL, CONCISE, SPEED = parser.parse()

    Reporter.print_problem_info(problem, CONCISE)

    solution_node = solver.solve()

    if solution_node is not None:
        Reporter.print_solution_stats(
            problem, solver, solution_node, CONCISE
        )
        Visualizer.visualize(
            problem,
            solver,
            solution_node,
            NO_VISUAL,
            SPEED
        )
    else:
        print("Solver failed to find a solution.")

if __name__ == "__main__":
    main()
