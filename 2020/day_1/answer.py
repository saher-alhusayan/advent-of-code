from input_data import data
from typing import Dict

# CRUDE SOLUTION #

# make list of entries
entries = [int(item) for item in data.split("\n")]

# part 1
part_1_answer = list(set([x * y for y in entries for x in entries if x + y == 2020]))

#  part 2
part_2_answer = list(
    set(
        [
            x * y * z
            for y in entries
            for x in entries
            for z in entries
            if x + y + z == 2020
        ]
    )
)
print(f"crude solution: part 1 answer is {part_1_answer[0]}")
print(f"crude solution: part 2 answer is {part_2_answer[0]}")


# SMART SOLUTION #

numbers = {int(item): 2020 - int(item) for item in data.split("\n")}


def part_1_answer(x):
    for number1, number2 in x.items():
        check_numnber = x.get(number2)
        if check_numnber is not None:
            return number1 * number2


answer = part_1_answer(numbers)
print(f"smart solutoin: part 1 answer is {answer}")


def part_2_answer(numbers: Dict):
    for number_one in list(numbers.keys()):
        for number_two in list(numbers.keys()):
            number_three = 2020 - (number_one + number_two)
            if number_three in list(numbers.keys()):
                return number_one * number_two * number_three


answer2 = part_2_answer(numbers)
print(f"smart solutoin: part 2 answer is {answer2}")
