from input_data import data
from typing import List, Tuple

# PART 1 #

# prepping data

lines = data.split("\n")
directions = [tuple(line.split(" ")) for line in lines]

# solution
commands = [
    (
        instruction,
        -int(value) if instruction == "up" else int(value),
    )
    for instruction, value in directions
]
part_1_answer = sum(
    [value for command, value in commands if command == "forward"]
) * sum([value for command, value in commands if command != "forward"])

print(f"answer to part 1: {part_1_answer}")

# PART 2 #
# solution


def calculate_answer(commands: List[Tuple[str, int]]) -> int:
    aim = 0
    horizental_position = 0
    depth = 0
    for command in commands:
        if command[0] in ["up", "down"]:
            aim += command[1]
        if command[0] == "forward":
            horizental_position += command[1]
            depth += command[1] * aim

    return depth * horizental_position


part_2_answer = calculate_answer(commands)
print(f"answer to part 2: {part_2_answer}")
