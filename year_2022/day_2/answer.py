from input_data import rounds
from typing import List, Dict, Tuple

# PREP DATA
rounds_ = rounds.split("\n")
list_of_rounds = [item.split(" ") for item in rounds_]


def find_total_score(
    list_of_rounds: List[str], rules: Dict[Tuple[str, str], int]
) -> bool:
    return sum([rules.get((round[0], round[1])) for round in list_of_rounds])


# PART ONE
RULES_PART_ONE = {
    ("A", "X"): 4,
    ("A", "Y"): 8,
    ("A", "Z"): 3,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 7,
    ("C", "Y"): 2,
    ("C", "Z"): 6,
}

print(find_total_score(list_of_rounds=list_of_rounds, rules=RULES_PART_ONE))

# PART 2

RULES_PART_TWO = {
    ("A", "X"): 3,
    ("A", "Y"): 4,
    ("A", "Z"): 8,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7,
}


print(find_total_score(list_of_rounds=list_of_rounds, rules=RULES_PART_TWO))
