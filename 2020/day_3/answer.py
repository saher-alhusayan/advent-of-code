from input_data import data
from typing import List

map = data.split("\n")
extended_map = [line * len(map) for line in map]


def calculate_trees(
    map: List[str], right_movement_index: int, down_movement_index: int
) -> int:
    trees = 0
    index = 0
    for pattern_number, pattern in enumerate(map):
        if pattern_number % down_movement_index == 0:
            if pattern[index] == "#":
                trees += 1
            index += right_movement_index
    return trees


answer = calculate_trees(extended_map, 3, 1)
print(answer)

# part 2
patterns = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total = 1
for pattern in patterns:
    right_movement_index, down_movement_index = pattern
    total = total * calculate_trees(
        map=extended_map,
        right_movement_index=right_movement_index,
        down_movement_index=down_movement_index,
    )

print(total)
