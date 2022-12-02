from input_data import rounds

# PREP DATA
rounds_ = rounds.split('\n')
list_of_rounds = [item.split(' ') for item in rounds_]

RULES = {
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
# PART 1
def determiine_if_player_two_wins(list_of_rounds: list[str]) -> bool:
    return RULES.get((list_of_rounds[0], list_of_rounds[1]))


outcome = list(map(determiine_if_player_two_wins, list_of_rounds))

print(sum(outcome))

# PART 2
