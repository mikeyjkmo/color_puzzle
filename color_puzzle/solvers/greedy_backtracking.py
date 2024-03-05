from color_puzzle.brick import Brick
from color_puzzle.parser import PuzzleConfig
from color_puzzle.solvers.lib import SolvedResult
from typing import NamedTuple


class GreedyBacktrackingResult(NamedTuple):
    score: int
    used_bricks: int


class GreedyBacktrackingSolver:
    """
    Finds an approximate solution by finding the best local solution at each column
    """

    def __init__(self, config: PuzzleConfig):
        self.config = config
        self.bricks = config["bricks"]
        self.bricks.sort(key=lambda brick: brick.total_value, reverse=True)

    def backtrack(
        self,
        first_brick_index: int,
        used_colors_bit_mask: int,
        used_bricks_bit_mask: int,
    ):
        """
        Backtrack to find the best local solution at each column
        """
        max_score = 0
        max_score_used_bricks = used_bricks_bit_mask

        used_colors_in_this_layer = set()

        for brick_idx in range(first_brick_index, len(self.bricks)):
            brick = self.bricks[brick_idx]

            if used_bricks_bit_mask & brick.id_bit_mask:
                continue

            if used_colors_bit_mask & brick.color_bit_mask:
                continue

            if brick.color_bit_mask in used_colors_in_this_layer:
                continue

            backtrack_result = self.backtrack(
                brick_idx + 1,
                used_colors_bit_mask | brick.color_bit_mask,
                used_bricks_bit_mask | brick.id_bit_mask,
            )

            new_score = brick.total_value + backtrack_result.score
            used_colors_in_this_layer.add(brick.color_bit_mask)

            if new_score > max_score:
                max_score = new_score
                max_score_used_bricks = backtrack_result.used_bricks

        return GreedyBacktrackingResult(max_score, max_score_used_bricks)

    def solve(self) -> SolvedResult:
        """
        Greedy algorithm that finds an approximate solution
        """
        num_cols = self.config["num_cols"]
        columns: list[list[Brick]] = [[] for _ in range(num_cols)]

        cumulative_used_bricks_in_each_col = [0 for _ in range(num_cols)]
        all_used_bricks_bit_mask = 0

        total_score = 0
        for col_idx in range(num_cols):
            score, used_bricks_in_col = self.backtrack(
                first_brick_index=0,
                used_colors_bit_mask=0,
                used_bricks_bit_mask=all_used_bricks_bit_mask,
            )

            total_score += score
            cumulative_used_bricks_in_each_col[col_idx] = used_bricks_in_col
            all_used_bricks_bit_mask = used_bricks_in_col

        for col_idx in range(num_cols):
            used_bricks_mask = (
                cumulative_used_bricks_in_each_col[col_idx]
                ^ cumulative_used_bricks_in_each_col[col_idx - 1]
                if col_idx > 0
                else cumulative_used_bricks_in_each_col[col_idx]
            )
            columns[col_idx] = self._filter_bricks_by_bit_mask(used_bricks_mask)

        return SolvedResult(total_score, columns)

    def _filter_bricks_by_bit_mask(self, bit_mask: int):
        """
        Given a bit mask representing the IDs of used bricks, return then
        bricks that are represented by it
        """
        return [brick for brick in self.bricks if brick.id_bit_mask & bit_mask]
