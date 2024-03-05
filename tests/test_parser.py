from color_puzzle.parser import Brick
from color_puzzle.parser import parse_puzzle_config


def test_brick_bit_mask():
    brick = Brick(1, {0: 3, 4: 2})
    assert brick.color_bit_mask == 17

    brick = Brick(1, {4: 2})
    assert brick.color_bit_mask == 16

    brick = Brick(1, {3: 2, 4: 9})
    assert brick.color_bit_mask == 24


def test_parser():
    config_str = """5 4 14
    0 3 4 2
    4 2
    3 2 4 9
    0 3
    1 4
    0 3 2 9
    0 3 1 1
    3 4
    0 1 1 2
    3 9
    2 1 4 1
    3 2
    2 9 3 1
    1 5"""

    result = parse_puzzle_config(config_str)

    assert result == {
        "num_colors": 5,
        "num_cols": 4,
        "bricks": [
            Brick(0, {0: 3, 4: 2}),
            Brick(1, {4: 2}),
            Brick(2, {3: 2, 4: 9}),
            Brick(3, {0: 3}),
            Brick(4, {1: 4}),
            Brick(5, {0: 3, 2: 9}),
            Brick(6, {0: 3, 1: 1}),
            Brick(7, {3: 4}),
            Brick(8, {0: 1, 1: 2}),
            Brick(9, {3: 9}),
            Brick(10, {2: 1, 4: 1}),
            Brick(11, {3: 2}),
            Brick(12, {2: 9, 3: 1}),
            Brick(13, {1: 5}),
        ],
    }
