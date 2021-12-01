from input_data import data
from typing import List

# PREPARE DATA #
depths = data.split("\n")
depth_measurements = [int(reading) for reading in depths]

# PART 1 #

# maybe neater? but less readable?
less_readable_answer_part_1 = len(
    [
        reading
        for index, reading in enumerate(depth_measurements)
        if index > 0 and depth_measurements[index - 1] < reading
    ]
)
print(f"less readable answer to part 1: {less_readable_answer_part_1}")

# more readable


def number_of_increased_measurements(readings: List[int]) -> int:
    total = 0
    for index, number in enumerate(readings):
        if index > 0 and number > readings[index - 1]:
            total += 1

    return total


part_1_answer = number_of_increased_measurements(depth_measurements)
print(f"answer to part 1: {part_1_answer}")

# PART 2 #

windows = [
    number + depth_measurements[index + 1] + depth_measurements[index + 2]
    for index, number in enumerate(depth_measurements)
    if index <= len(depth_measurements) - 3
]


part_2_answer = number_of_increased_measurements(windows)
print(f"answer to part 2: {part_2_answer}")
