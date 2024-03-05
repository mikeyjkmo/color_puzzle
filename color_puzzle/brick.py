from typing import Optional


class Brick:
    def __init__(self, brick_id: int, color_values: dict[int, int]):
        self.brick_id = brick_id
        self.color_values = color_values
        self.total_value = sum(color_values.values())
        self.color_bit_mask = sum(1 << color for color in self.color_values.keys())
        self.id_bit_mask = 1 << brick_id

    def __str__(self):
        return " ".join(
            f"{color_index}: {value}"
            for color_index, value in self.color_values.items()
            if value is not None
        )

    def __repr__(self):
        return f"Brick(brick_id={self.brick_id}, {self.color_values})"

    def __eq__(self, other):
        return self.color_values == other.color_values and self.brick_id == other.brick_id

    @staticmethod
    def from_string(brick_id: int, brick_str: str):
        """
        Create a brick from a string
        """
        nums = brick_str.split(" ")

        if len(nums) % 2 != 0:
            raise ValueError(f"Invalid brick string: {brick_str}")

        colors: dict[int, int] = {}

        current_color: Optional[int] = None

        for idx, n in enumerate(nums):
            if idx % 2 == 0:
                current_color = int(n)
            elif current_color is not None:
                colors[current_color] = int(n)

        return Brick(brick_id, colors)
