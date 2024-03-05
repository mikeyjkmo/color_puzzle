from color_puzzle.brick import Brick
from color_puzzle.parser import PuzzleConfig
from color_puzzle.solvers.lib import SolvedResult


class GreedySolver:
    """
    Finds an approximate solution in polynomial time
    """
    def __init__(self, config: PuzzleConfig):
        self.config = config
        self.bricks = config["bricks"]
        self.bricks.sort(key=lambda brick: brick.total_value, reverse=True)

    def solve(self) -> SolvedResult:
        """
        Greedy algorithm that finds an approximate solution in polynomial time
        """
        num_cols = self.config["num_cols"]
        columns: list[list[Brick]] = [[] for _ in range(num_cols)]
        column_bit_masks = [0 for _ in range(num_cols)]

        for brick in self.bricks:
            for col_idx in range(num_cols):
                if column_bit_masks[col_idx] & brick.color_bit_mask:
                    continue

                columns[col_idx].append(brick)
                column_bit_masks[col_idx] |= brick.color_bit_mask
                break

        score = sum(sum(brick.total_value for brick in col) for col in columns)

        result = [str(score)]
        for col in columns:
            result.append(" ".join([str(brick.brick_id) for brick in col]))

        return SolvedResult(score, columns)
