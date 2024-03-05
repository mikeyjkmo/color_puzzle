from color_puzzle.solvers.greedy_backtracking import GreedyBacktrackingSolver
from color_puzzle.parser import parse_puzzle_with_readable, StdInReadable

def main():
    config = parse_puzzle_with_readable(StdInReadable())
    solver = GreedyBacktrackingSolver(config)
    result = solver.solve()
    print(result)


if __name__ == "__main__":
    main()
