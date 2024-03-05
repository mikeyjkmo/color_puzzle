from typing import Sequence, NamedTuple
from color_puzzle.solvers.lib import SolvedResult
from color_puzzle.parser import PuzzleConfig
from color_puzzle.brick import Brick


class BacktrackResult(NamedTuple):
    score: int
    used_bricks: int
    cumulative_used_bricks_in_each_column: list[int]


class FullBacktrackingSolver:
    def __init__(self, config: PuzzleConfig):
        self.config = config
        self.bricks = config["bricks"]
        self.bricks.sort(key=lambda brick: brick.total_value, reverse=True)
        self.cache: dict[int, BacktrackResult] = {}

    def backtrack(
        self,
        bricks: Sequence[Brick],
        col_idx: int,
        used_colors: int,
        used_bricks_so_far: int,
        cumulative_used_bricks_in_each_column: list[int]
    ) -> BacktrackResult:
        num_cols = self.config["num_cols"]
        max_score = 0
        max_score_used_bricks_so_far = used_bricks_so_far
        max_score_col_bit_masks = cumulative_used_bricks_in_each_column

        if used_bricks_so_far in self.cache:
            return self.cache[used_bricks_so_far]

        if col_idx == num_cols:
            # Columns are exhausted
            return BacktrackResult(
                score=0,
                used_bricks=used_bricks_so_far,
                cumulative_used_bricks_in_each_column=cumulative_used_bricks_in_each_column,
            )

        brick_found = False
        brick_colors_backtracked_in_this_layer = set()

        for brick_idx, brick in enumerate(bricks):
            if used_bricks_so_far & brick.id_bit_mask:
                continue

            if used_colors & brick.color_bit_mask:
                continue

            if brick.color_bit_mask in brick_colors_backtracked_in_this_layer:
                continue

            brick_found = True

            backtrack_result = self.backtrack(
                bricks=bricks[brick_idx + 1 :],
                col_idx=col_idx,
                used_colors=used_colors | brick.color_bit_mask,
                used_bricks_so_far=used_bricks_so_far | brick.id_bit_mask,
                cumulative_used_bricks_in_each_column=cumulative_used_bricks_in_each_column,
            )
            new_score = brick.total_value + backtrack_result.score

            brick_colors_backtracked_in_this_layer.add(brick.color_bit_mask)

            if new_score > max_score:
                max_score = new_score
                max_score_used_bricks_so_far = backtrack_result.used_bricks
                max_score_col_bit_masks = (
                    backtrack_result.cumulative_used_bricks_in_each_column
                )

        if not brick_found:
            # No suitable brick, move onto the next column
            return self.backtrack(
                bricks=self.bricks,
                col_idx=col_idx + 1,
                used_colors=0,
                used_bricks_so_far=used_bricks_so_far,
                cumulative_used_bricks_in_each_column=[
                    *cumulative_used_bricks_in_each_column,
                    used_bricks_so_far,
                ]
            )

        self.cache[used_bricks_so_far] = BacktrackResult(
            score=max_score,
            used_bricks=max_score_used_bricks_so_far,
            cumulative_used_bricks_in_each_column=cumulative_used_bricks_in_each_column,
        )

        return BacktrackResult(
            score=max_score,
            used_bricks=max_score_used_bricks_so_far,
            cumulative_used_bricks_in_each_column=max_score_col_bit_masks,
        )

    def _reset_cache(self):
        self.cache = {}

    def solve(self) -> SolvedResult:
        """
        Exponential algorithm with memoization
        """
        self._reset_cache()

        max_score, _, cumulative_used_bricks_in_each_column = self.backtrack(
            bricks=self.bricks,
            col_idx=0,
            used_colors=0,
            used_bricks_so_far=0,
            cumulative_used_bricks_in_each_column=[],
        )
        normalized_bit_masks = self._normalize_used_brick_bit_masks(
            cumulative_used_bricks_in_each_column
        )

        return SolvedResult(
            max_score,
            [
                self._filter_bricks_by_bit_mask(col_mask)
                for col_mask in normalized_bit_masks
            ],
        )

    def _filter_bricks_by_bit_mask(self, bit_mask: int):
        """
        Given a bit mask representing the IDs of used bricks, return then
        bricks that are represented by it
        """
        return [brick for brick in self.bricks if brick.id_bit_mask & bit_mask]

    def _normalize_used_brick_bit_masks(
        self, cumulative_used_bricks_in_each_column: list[int]
    ):
        """
        Given a list of cumulative bit masks, normalize them so that each
        index only represents the bit mask of the bricks used in that column
        """
        return [
            (
                bit_mask
                if idx == 0
                else bit_mask ^ cumulative_used_bricks_in_each_column[idx - 1]
            )
            for idx, bit_mask in enumerate(cumulative_used_bricks_in_each_column)
        ]
