from input_data import ids
from typing import List

import functools


sections = ids.split("\n")
section_ids = [item.split(",") for item in sections]


def determine_overlap(sections: List[str], part: int) -> bool:
    first_section, second_section = sections
    first_section_a, first_section_b = first_section.split("-")
    second_section_a, second_section_b = second_section.split("-")
    first_section_range = set(range(int(first_section_a), int(first_section_b) + 1))
    second_section_range = set(range(int(second_section_a), int(second_section_b) + 1))
    if part == 1:
        if first_section_range.issubset(
            second_section_range
        ) or second_section_range.issubset(first_section_range):
            return True
        else:
            return False
    elif part == 2:
        overlap = first_section_range & second_section_range
        return bool(overlap)
    else:
        raise ValueError(f"Part passed as {part} is neither 1 or 2")


overlap_map_part_one = map(functools.partial(determine_overlap, part=1), section_ids)
overlap_map_part_two = map(functools.partial(determine_overlap, part=2), section_ids)


print(f"Part one answer: {len([item for item in overlap_map_part_one if item])}")
print(f"Part two answer: {len([item for item in overlap_map_part_two if item])}")
