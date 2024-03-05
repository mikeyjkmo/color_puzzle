# Exercise

Solving a Colourful Puzzle
You have 7 days to provide a solution for this exercise, however we anticipate that it should be
possible to complete the challenge in less than three hours. The tests should execute in
sub-second times for all of our input datasets. "Timeout" indicates that the solution is taking too long
to execute and your algorithm needs improvement. It is possible to pass the tests with simple
approaches but extra credit will be given for solutions that achieve higher scores.
In this problem we are going to solve a two-dimensional puzzle.
The board is N units in height and M units in width. Each row of the board is assigned a unique
colour. Puzzle bricks are pieces that contain at least one coloured token and a maximum of N
coloured tokens. Each colour can occur at most once in every brick. Each brick also has a value
associated with the coloured tokens, which adds to the score of the solution when placed on the
puzzle board.
When placing bricks on the board, the following rules apply:

1. Each brick can be used at most once,
2. A brick can only be placed in a column if it is compatible with all of the bricks that have
already been placed in that column.
3. Two bricks are compatible if they do not have any colours in common so, for example, a
brick with colours {0,2} is compatible with a brick that has colours {1, 3}. When placed in a
column, these bricks would be compatible with any other brick that does not contain any of
the colours {0, 1, 2, 3} and so forth.

Your task is to find a valid placement of bricks on the board such that their total score is
maximized.

## Example

```
5 4 14
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
1 5
```

Your program should output M + 1 lines.
● The first line containing the overall score of your solution,
● each of the following M lines containing the 0-based indexes (specified in the input data) of
the bricks used in each column.
The output for the example would be:

```
71
6 7 1
3 4 10 9
0 13 12
5 2
```

# Solution

## Requirments

- Python 3.8+
- `python-poetry`1.7+ (optional)

## Running without Poetry

### Install

Create a virtual env
```bash
$ python -m venv .venv
```

Activate the virtual env
```bash
$ source .venv/bin/activate
```

Install the dependencies
```bash
$ pip install -r requirements.txt
```

### Run tests

```bash
$ make tests
```

### Run main

```bash
$ make run < input.txt
```

## Running with Poetry

### Install

Install the dependencies
```bash
$ poetry install
```

### Run tests

```bash
$ poetry run pytest
```

### Run main

```bash
$ poetry run color_puzzle/main.py < input.txt
```
