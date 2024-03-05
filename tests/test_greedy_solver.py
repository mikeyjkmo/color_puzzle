from color_puzzle.parser import parse_puzzle_config
from color_puzzle.solvers.greedy import GreedySolver


def test_example_3_3_12():
    # Given
    config_str = """3 3 12
    0 27 1 26 2 19
    0 25 1 3 2 28
    0 5 1 24 2 3
    0 21 1 11 2 23
    2 16
    0 9 1 29 2 14
    2 16
    2 14
    0 28
    1 23
    0 25
    0 1 1 6
    """
    puzzle_config = parse_puzzle_config(config_str)

    # When
    result = GreedySolver(puzzle_config).solve()

    # Then
    expected = [
        '183',
        '0',
        '1',
        '3',
    ]
    assert result.to_list() == expected


def test_example_5_4_14():
    # Given
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
    puzzle_config = parse_puzzle_config(config_str)

    # When
    result = GreedySolver(puzzle_config).solve()

    # Then
    expected = [
        "71",
        "5 2 13",
        "12 0 4",
        "9 6 1",
        "7 3 10",
    ]
    assert result.to_list() == expected


def test_example_5_5_20():
    # Given
    config_str = """5 5 20
    2 9
    0 11 4 28
    0 23 3 6 4 18
    3 11 4 3
    0 10 1 29 2 10 3 16 4 4
    0 22 1 29 3 17 4 18
    0 3 1 3 3 7
    0 15 2 14 3 12 4 7
    2 27 4 22
    2 18 3 6
    2 27
    0 22 1 12 2 13 3 16 4 1
    0 17 1 26 2 13 3 6 4 24
    2 12 3 23
    0 2 1 12 2 20 3 10 4 9
    0 17 1 10
    1 10 2 29 3 4
    1 19 2 16 3 20 4 20
    1 17 2 7 4 5
    0 30 2 28
    """
    puzzle_config = parse_puzzle_config(config_str)

    # When
    result = GreedySolver(puzzle_config).solve()

    # Then
    expected = [
        "407",
        "5 10",
        "12",
        "17",
        "4",
        "11",
    ]

    assert result.to_list() == expected


def test_example_5_5_50():
    # Given
    config_str = """5 5 50
    1 23 4 15
    0 24 4 1
    0 30 1 12 2 12 3 12 4 7
    1 4 2 19 3 9
    2 3 3 19 4 20
    0 24 1 9 3 3 4 27
    0 8 1 1 3 17 4 30
    1 18 4 6
    0 30
    0 3 1 29 2 4 3 21 4 2
    0 27 2 26 3 6
    1 1 2 6
    1 2 2 1 3 12
    0 15 1 23 2 13 3 11
    3 19
    0 3 1 29 2 6 3 20 4 4
    2 5
    0 18 1 11 2 24 4 17
    1 7
    1 16
    1 6 3 11
    3 3 4 24
    3 11
    0 1 3 11 4 9
    0 29 1 24 2 22 3 20 4 14
    0 26 1 19 2 19 3 30 4 14
    0 3 4 27
    0 26 4 24
    3 24 4 23
    1 8 2 29 3 6 4 22
    0 6 1 24 2 19 3 25 4 12
    0 19 2 10 4 18
    0 29 1 24 2 24 4 1
    0 20 3 10
    0 21 2 19 3 2 4 3
    3 18
    1 3 2 1 3 25 4 4
    0 20 1 15 3 2 4 12
    0 12 1 12 2 11 3 7
    0 28 1 25 2 27 3 19 4 30
    0 5 1 24 2 11 3 24
    2 23 3 7
    0 28 2 27 4 27
    2 2
    0 30
    0 17 1 11 2 3 3 24 4 1
    1 14 2 15
    0 26 1 22 3 28 4 17
    1 30 2 4 4 21
    0 26"""
    puzzle_config = parse_puzzle_config(config_str)

    # When
    result = GreedySolver(puzzle_config).solve()

    # Then
    expected = [
        "530",
        "39",
        "24",
        "25",
        "47 16",
        "30",
    ]
    assert result.to_list() == expected


def test_example_10_10_40():
    # Given
    config_str = """10 10 40
    0 21 1 22 2 15 3 23 4 9 5 26 6 26 7 2 8 21 9 28
    0 14 2 17 5 12 6 9 8 2
    1 14
    2 4 3 5 4 22 5 5 6 13 7 27 8 11 9 15
    0 11 1 15 2 5 3 28 4 5 8 20
    0 25 8 27
    2 10 3 28 5 11 6 29 8 9 9 16
    3 5 4 26 5 14 6 1 7 28 9 20
    1 3 4 28 9 20
    3 25 6 5 9 18
    0 18 1 9 3 14 4 18 7 12 8 15
    0 23 1 24 2 2 4 24 5 9 6 3 7 17 8 11 9 9
    0 12 1 18 2 23 5 20 6 8 7 25 9 13
    1 6 5 5 6 1 7 7 9 24
    2 25
    1 28 2 29 3 21 5 27 6 17 9 12
    0 15 1 7 2 11 4 19 5 20 7 24 8 30 9 7
    9 10
    0 21 1 19 3 2 4 16 5 13 7 17 9 6
    0 4 1 29 2 10 4 22 5 7 6 22 7 10 8 11 9 17
    1 6 6 30 8 21
    5 28 7 14
    1 7 4 4 8 1 9 10
    0 18 1 7 2 16 3 23 4 1 5 13 6 1 8 7 9 17
    0 16 4 14 6 1
    0 25 1 15 2 19 3 10 4 1 5 27 6 14 7 12 8 28 9 11
    0 23 1 29 3 28 4 2 5 3 6 13 7 16 8 26 9 14
    2 24 3 10 4 16 5 11 7 14
    2 1 5 13 7 10
    1 30 4 10 7 17
    2 19 3 2 8 19
    0 24 1 22 3 25 4 11 6 26 7 13 9 7
    3 19 6 14 7 28 9 2
    2 29 4 3 6 6 8 19
    1 7 4 26 6 30
    2 4 3 6 4 10 5 29 7 29 8 22
    2 12 7 25 8 12 9 23
    2 24 4 26 5 2 6 14 8 19 9 12
    0 27 1 30 2 9 3 4 4 19 5 2 6 9 7 12 8 3 9 16
    0 15 1 11 2 19 3 10 4 4 5 1 6 24 7 28 8 12 9 13
    """
    puzzle_config = parse_puzzle_config(config_str)

    # When
    result = GreedySolver(puzzle_config).solve()

    # Then
    expected = [
        "1503",
        "0",
        "25",
        "26 14",
        "39",
        "15 5",
        "16",
        "19",
        "38",
        "31",
        "11",
    ]
    assert result.to_list() == expected
