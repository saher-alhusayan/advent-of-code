from input_data import data
from typing import Dict, Tuple
from itertools import product


# MAKE DATA #


def make_grid(d: str) -> Dict[Tuple[int, int], str]:
    lines = d.split("\n")
    grid = {}
    for index, line in enumerate(lines):
        for seat_number, seat in enumerate(line):
            grid.update({(index, seat_number): seat})
    return grid


grid = make_grid(data)

# PART 1 #


def apply_rules_to_seat(grid: Dict[Tuple[int, int], str]) -> Dict[Tuple[int, int], str]:
    new_dict = {}
    for (y, x), status in grid.items():
        keys = list(product([y, y + 1, y - 1], [x, x + 1, x - 1]))
        keys.remove((y, x))
        adjacent_seats = [grid.get(key) for key in keys]
        if status == "L" and "#" not in adjacent_seats:
            new_dict.update({(y, x): "#"})
            continue
        if status == "#" and adjacent_seats.count("#") >= 4:
            new_dict.update({(y, x): "L"})
            continue
        else:
            new_dict.update({(y, x): status})
    return new_dict


def get_part_1_answer(grid):
    new = apply_rules_to_seat(grid=grid)
    if new == grid:
        return new
    else:
        return get_part_1_answer(grid=new)


print(list(get_part_1_answer(grid).values()).count("#"))


# PART 2 #
def apply_rules_to_seat_part_2(
    grid: Dict[Tuple[int, int], str]
) -> Dict[Tuple[int, int], str]:
    new_dict = {}
    for (y, x), status in grid.items():

        adjacent_seats = get_adjacent_seats(y, x, grid)
        if status == "L" and "#" not in adjacent_seats:
            new_dict.update({(y, x): "#"})
            continue
        if status == "#" and adjacent_seats.count("#") >= 5:
            new_dict.update({(y, x): "L"})
            continue
        else:
            new_dict.update({(y, x): status})
    return new_dict


def get_adjacent_seats(y, x, grid):
    coords = (y, x)
    lst = []
    value = "."
    y, x = coords
    while value == ".":
        x += 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)

    value = "."
    y, x = coords
    while value == ".":
        x -= 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)

    value = "."
    y, x = coords
    while value == ".":
        y -= 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)

    value = "."
    y, x = coords
    while value == ".":
        y += 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)

    value = "."
    y, x = coords
    while value == ".":
        y += 1
        x += 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)

    value = "."
    y, x = coords
    while value == ".":
        y -= 1
        x -= 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)

    value = "."
    y, x = coords
    while value == ".":
        y += 1
        x -= 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)

    value = "."
    y, x = coords
    while value == ".":
        y -= 1
        x += 1
        value = grid.get((y, x))
        if value and value != ".":
            lst.append(value)
    return lst


def get_part_2_answer(grid):
    new = apply_rules_to_seat_part_2(grid=grid)
    if new == grid:
        return new
    else:
        return get_part_2_answer(grid=new)


print(list(get_part_2_answer(grid).values()).count("#"))
