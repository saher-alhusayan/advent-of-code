from input_data import moves as data
from typing import List, Tuple

moves = data.split("\n")
moves = [item.split(" ") for item in moves]

INSTRUCTION = {
    "R": (1, 0),
    "D": (0, -1),
    "L": (-1, 0),
    "U": (0, 1),
}


def same_level_move(
    distance: str, direction: str, head: Tuple[int, int], tail: Tuple[int, int]
):
    temp_path = []
    for _ in range(int(distance)):
        head = (
            head[0] + INSTRUCTION[direction][0],
            head[1] + INSTRUCTION[direction][1],
        )
        temp_path.append(head)
    temp_path.pop()
    if temp_path:
        tail = temp_path[-1]
    return temp_path, head, tail


def different_level_move(
    distance: str, direction: str, head: Tuple[int, int], tail: Tuple[int, int]
):
    temp_path = []
    for _ in range(int(distance)):
        head = (
            head[0] + INSTRUCTION[direction][0],
            head[1] + INSTRUCTION[direction][1],
        )
        temp_path.append(head)
    if int(distance) <= 2:
        return [], head, tail
    else:
        temp_path.pop()
        if temp_path:
            tail = temp_path[-1]
        temp_path.reverse()
        temp_path.pop()
    return temp_path, head, tail


def get_path(moves: List[Tuple[str, int]]) -> List[Tuple[int, int]]:
    head = (0, 0)
    tail = (0, 0)
    path = []

    for direction, distance in moves:
        temp_path = []
        if (direction in ["R", "L"] and head[1] == tail[1]) or (
            direction in ["U", "D"] and head[0] == tail[0]
        ):
            temp_path, head, tail = same_level_move(distance, direction, head, tail)
            [path.append(position) for position in temp_path]

        if direction in ["R", "L"] and head[1] != tail[1]:
            if (head[0] < tail[0] and direction == "R") or (
                head[0] > tail[0] and direction == "L"
            ):
                temp_path, head, tail = different_level_move(
                    distance, direction, head, tail
                )
                [path.append(position) for position in temp_path]

            elif head[0] >= tail[0] and direction == "R":
                if head[0] > tail[0]:
                    path.append(head)
                temp_path, head, tail = same_level_move(distance, direction, head, tail)
                [path.append(position) for position in temp_path]

            elif head[0] <= tail[0] and direction == "L":
                if head[0] < tail[0]:
                    path.append(head)
                temp_path, head, tail = same_level_move(distance, direction, head, tail)
                [path.append(position) for position in temp_path]

        if direction in ["U", "D"] and head[0] != tail[0]:
            if (head[1] < tail[1] and direction == "U") or (
                head[1] > tail[1] and direction == "D"
            ):
                temp_path, head, tail = different_level_move(
                    distance, direction, head, tail
                )
                [path.append(position) for position in temp_path]

            elif head[1] >= tail[1] and direction == "U":
                if head[1] > tail[1]:
                    path.append(head)
                temp_path, head, tail = same_level_move(distance, direction, head, tail)
                [path.append(position) for position in temp_path]

            elif head[1] <= tail[1] and direction == "D":
                if head[1] < tail[1]:
                    path.append(head)
                temp_path, head, tail = same_level_move(distance, direction, head, tail)
                [path.append(position) for position in temp_path]

    return path


print(len(set(get_path(moves))))
