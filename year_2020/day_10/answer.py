from input_data import data
from collections import Counter


ratings = [int(rating) for rating in data.split("\n")]

# PART 1 #

ratings.append(0)  # charging outlet joltage is 0
ratings.append(max(ratings) + 3)  #  adding the devices's joltage

sorted_list = sorted(ratings)

zipped = list(zip(sorted_list, sorted_list[1:]))


def _b_minus_a(t: tuple) -> int:
    first_number, second_number = t
    return second_number - first_number


mapped = list(map(_b_minus_a, zipped))
differences = dict(Counter(mapped))

# no try accept as assuming there will definitely be 1 and 3 differences
print(f"answer to part 1: " f"{differences.get(1) * differences.get(3)}")

# PART 2 #

volatages = sorted([int(volatage) for volatage in data.split("\n")])
d = {volatages.pop(): 1}

for n in list(reversed(volatages)) + [0]:
    d[n] = d.get(n + 1, 0) + d.get(n + 2, 0) + d.get(n + 3, 0)

print(f"answer to part 2: {d[0]}")
