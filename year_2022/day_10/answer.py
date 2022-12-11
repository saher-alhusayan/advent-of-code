from input_data import instructions as data
from typing import List

instructions = data.split('\n')

# PART 1

def get_answer(instructions: List[str]) -> int:
    values_of_x_to_return = []
    cycle = 0
    value_of_x = 1
    for instruction in instructions:
        if instruction == "noop":
            cycle += 1
            if cycle in list(range(20, len(instructions) * 2, 40)):
                values_of_x_to_return.append(cycle * value_of_x)
        else:
            num = int(instruction.split(' ')[1])
            cycle += 1
            if cycle in list(range(20, len(instructions) * 2, 40)):
                values_of_x_to_return.append(cycle * value_of_x)
            cycle += 1
            if cycle in list(range(20, len(instructions) * 2, 40)):
                values_of_x_to_return.append(cycle * value_of_x)
            value_of_x += num
    return sum(values_of_x_to_return)

print(get_answer(instructions))


