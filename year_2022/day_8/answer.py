from input_data import grid as data
from typing import List

# PREP DATA

input = data.split("\n")

horizontal_grid = []
for tree_line in input:
    horizontal_grid.append([int(i) for i in tree_line])

vertical_grid = list(zip(*horizontal_grid))


def scan(line: List[int]) -> List[bool]:
    outcome = []
    for index, tree in enumerate(line[1:-1], 1):
        if all(bool(tree > x) for x in line[index + 1 :]) or all(
            bool(tree > x) for x in line[:index]
        ):
            outcome.append(True)
        else:
            outcome.append(False)
    return outcome


# PART 1

horizontal = list(map(scan, horizontal_grid))
vertical = list(map(scan, vertical_grid))

joint_outcomes = []
for i, result in enumerate(horizontal[1:-1]):
    for x, tree in enumerate(result):
        joint_outcomes.append([tree, vertical[1:-1][x][i]])


interior = [any(i) for i in joint_outcomes]
interior_length = len([i for i in interior if i])
grid_edge = (len(horizontal_grid[0]) - 1) * 4
total = grid_edge + interior_length
print(total)

# PART 2


def find_blocker_tree(line, x):
    ls = []
    for item in line:
        if item < x:
            ls.append(item)
        else:
            ls.append(item)
            break
    return len(ls)


def get_scenic_view(horizontal: List[int], vertical: List[int]) -> List[int]:
    outcome = []
    for index, line in enumerate(horizontal[1:-1]):
        for index2, tree in enumerate(line[1:-1]):
            line_to_check_right = horizontal[index + 1][index2 + 2 :]
            right_view = find_blocker_tree(line_to_check_right, tree)

            line_to_check_left = horizontal[index + 1][: index2 + 1]
            line_to_check_left.reverse()
            left_view = find_blocker_tree(line_to_check_left, tree)

            line_to_check_down = vertical[index2 + 1][index + 2 :]
            downwards_view = find_blocker_tree(line_to_check_down, tree)

            line_to_check_up = vertical[index2 + 1][: index + 1]
            line_to_check_up = list(line_to_check_up)
            line_to_check_up.reverse()

            upwards_view = find_blocker_tree(line_to_check_up, tree)

            outcome.append(left_view * right_view * upwards_view * downwards_view)
    return outcome


all = get_scenic_view(horizontal=horizontal_grid, vertical=vertical_grid)
print(max(all))
