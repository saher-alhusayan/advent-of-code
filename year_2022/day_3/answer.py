from input_data import compartments
import string
from typing import Tuple, List, Union

# PREP DATA

comps = compartments.split("\n")
comparts = [(comp[: len(comp) // 2], comp[len(comp) // 2 :]) for comp in comps]

a_to_z = string.ascii_lowercase[:27]
A_to_Z = string.ascii_uppercase[:27]

dict1 = dict(
    zip(
        a_to_z,
        range(1, 27),
    )
)

dict2 = dict(
    zip(
        A_to_Z,
        range(27, 53),
    )
)

PRIORITIES = {**dict1, **dict2}

# PART 1


def find_sum_of_priorities(compartment: Union[Tuple[str, str], List[str]]) -> int:
    if len(compartment) == 2:
        first_comp, second_comp = compartment
        priotrity = set("".join(first_comp)).intersection(set("".join(second_comp)))
        return PRIORITIES.get(list(priotrity)[0])
    elif len(compartment) == 3:
        first_comp, second_comp, third_comp = compartment
        priotrity = (
            set("".join(first_comp))
            .intersection(set("".join(second_comp)))
            .intersection(set("".join(third_comp)))
        )
        return PRIORITIES.get(list(priotrity)[0])
    else:
        raise RuntimeError(
            f"Length of compartment is {len(compartment)}, which is not 2 or 3"
        )


print(sum(list(map(find_sum_of_priorities, comparts))))


# PART 2
compartments_in_threes = []
for i, x in enumerate(list(range(1, len(comps) // 3 + 1))):
    compartments_in_threes.append(comps[i * 3 : x * 3])

print(sum(list(map(find_sum_of_priorities, compartments_in_threes))))
