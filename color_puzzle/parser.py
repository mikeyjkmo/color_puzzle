from typing import TypedDict, Protocol

from color_puzzle.brick import Brick


class PuzzleConfig(TypedDict):
    num_colors: int
    num_cols: int
    bricks: list[Brick]


class Readable(Protocol):
    def readline(self) -> str:
        ...


class StdInReadable:
    def readline(self) -> str:
        return input()


class StringReadable:
    def __init__(self, lines: str):
        self.lines = lines.split("\n")
        self.idx = 0

    def readline(self) -> str:
        line = self.lines[self.idx]
        self.idx += 1
        return line


def parse_puzzle_with_readable(readable: Readable) -> PuzzleConfig:
    """
    Parse puzzle configuration using a Readable object
    """
    raw_puzzle_params = readable.readline().strip()
    [num_colors, num_cols, num_bricks] = raw_puzzle_params.split(" ")

    bricks = []
    for brick_idx in range(int(num_bricks)):
        raw_brick = readable.readline().strip()
        bricks.append(Brick.from_string(brick_idx, raw_brick))

    return {
        "num_colors": int(num_colors),
        "num_cols": int(num_cols),
        "bricks": bricks,
    }


def parse_puzzle_config(raw_puzzle_config: str) -> PuzzleConfig:
    """
    Helper function used for testing
    """
    return parse_puzzle_with_readable(StringReadable(raw_puzzle_config))
