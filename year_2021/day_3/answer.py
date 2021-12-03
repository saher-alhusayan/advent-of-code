from input_data import data
from collections import Counter
from typing import List

binaries = data.split("\n")

#  make list of lists containing separate binary digits for each binary
unpacked_binaries: List[List[str]] = [list(lst) for lst in binaries]

#  create tuples of same indexes of all binaries
zipped = zip(*unpacked_binaries)

# use Counter to get the most common in each tuple
counter_objects = (Counter(c).most_common(1)[0][0] for c in zipped)

# make gama binary
gama = "".join([*counter_objects])

# make epsilon binary
epsilon = "".join(["1" if digit == "0" else "0" for digit in gama])

# answer
print(f"answer to part 1: {int(gama, 2) * int(epsilon, 2)}")
