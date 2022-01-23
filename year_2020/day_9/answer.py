import input_data
from typing import List
from itertools import combinations

data = [int(item) for item in input_data.sequence.split("\n")]


# PART 1


def _find_invalid_number(data: List[int], preamble: int) -> int:
    for index, number in enumerate(data[preamble:]):
        end_of_preamble = index + preamble
        if number not in list(
            map(sum, list(combinations(data[index:end_of_preamble], 2)))
        ):
            return number


part_1_answer = _find_invalid_number(data, 25)
print(f"part 1 answer: {part_1_answer}")

# PART 2


def _find_set(data: List[int], invalid_number: int) -> int:
    for index, _ in enumerate(data):
        target = 0
        new_index = index
        lst = []
        while target < invalid_number:
            target += data[new_index]
            lst.append(data[new_index])
            new_index += 1
            if target == invalid_number:
                return sum([max(lst), min(lst)])


part_2_answer = _find_set(data, part_1_answer)
print(f"part 2 answer: {part_2_answer}")
