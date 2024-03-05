from typing import Sequence, NamedTuple
from dataclasses import dataclass
from color_puzzle.brick import Brick


class BacktrackResult(NamedTuple):
    score: int
    used_bricks: int
    cumulative_used_bricks_in_each_column: list[int]


@dataclass
class SolvedResult:
    score: int
    columns: Sequence[Sequence[Brick]]

    def to_list(self) -> list[str]:
        result: list[str] = [str(self.score)]
        for bricks in self.columns:
            result.append(" ".join([str(brick.brick_id) for brick in bricks]))
        return result

    def __str__(self):
        return "\n".join(self.to_list())
