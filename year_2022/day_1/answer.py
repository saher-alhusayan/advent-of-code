from input_data import calories
from collections import Counter
# PREP DATA

groups = calories.split("\n\n")

list_of_groups = [item.split("\n") for item in groups]

groups_as_integers = [list(map(int, group)) for group in list_of_groups]

# PART ONE
sums_of_groups = [sum(item) for item in groups_as_integers]
print(max(sums_of_groups))


# PART TWO

print(sum(sorted(sums_of_groups, reverse=True)[:3]))


