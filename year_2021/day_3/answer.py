from input_data import data
from collections import Counter
from typing import List, Tuple

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


# Part 2 #

# Slightly ugly and long solution #


def _get_binaries_with_most_or_least_common_binary(
    binaries: List[str], index: int, counting_most: bool
) -> List[str]:
    #  make list of lists containing separate binary digits for each binary
    unpacked_binaries: List[List[str]] = [list(lst) for lst in binaries]

    #  create tuples of same indexes of all binaries
    zipped = zip(*unpacked_binaries)

    binaries_at_certain_index = list(zipped)[index]
    try:
        most_common, least_common = Counter(binaries_at_certain_index).most_common()
    except ValueError:
        digit, _ = Counter(binaries_at_certain_index).most_common()[0]
        return [binary for binary in binaries if binary[index] == str(digit)]

    digit = _determine_digit(most_common, least_common, counting_most)

    return [binary for binary in binaries if binary[index] == str(digit)]


def _determine_digit(
    most_common: Tuple[str, int],
    least_common: Tuple[str, int],
    counting_most: bool,
) -> str:
    d1, c1 = most_common
    d2, c2 = least_common
    if counting_most is True:
        if c1 == c2:
            return "1"
        elif c1 > c2:
            return d1
        else:
            return d2
    else:
        if c1 == c2:
            return "0"
        elif c1 > c2:
            return d2
        else:
            return d1


def _get_o2_generator_or_co2_scrubber(binaries: List[str], counting_most: bool) -> str:
    index = 0
    while len(binaries) > 1 and index < 12:
        binaries = _get_binaries_with_most_or_least_common_binary(
            binaries, index, counting_most
        )
        index += 1
    return binaries[0]


o2 = _get_o2_generator_or_co2_scrubber(binaries, True)
co2 = _get_o2_generator_or_co2_scrubber(binaries, False)

print(f"answer to part 2: {int(o2, 2) * int(co2, 2)}")
