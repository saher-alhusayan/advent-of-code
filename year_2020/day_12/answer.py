from input_data import data, example
from typing import List, Dict

instructions = [instruction for instruction in data.split("\n")]
example_ = [instruction for instruction in example.split("\n")]


def interpret_instructions(instructions: List[str]) -> Dict[str, int]:
    d = {"E": 0, "N": 0, "S": 0, "W": 0}
    direction = "E"
    for instruction in instructions:
        letter = instruction[0]
        value = int(instruction[1:])
        if letter == "F":
            d[direction] += value
            continue
        if letter in ["L", "R"]:
            direction = _determine_direction(
                current_direction=direction, instruction=letter, degree=value
            )
            continue
        d[letter] += value
    return d


def _determine_direction(current_direction: str, instruction: str, degree: int) -> str:
    right_mapping = {
        "E": {0: "E", 1: "S", 2: "W", 3: "N", 4: "E"},
        "N": {0: "N", 1: "E", 2: "S", 3: "W", 4: "N"},
        "S": {0: "S", 1: "W", 2: "N", 3: "E", 4: "S"},
        "W": {0: "W", 1: "N", 2: "E", 3: "S", 4: "W"},
    }
    left_mapping = {
        "E": {0: "E", 1: "N", 2: "W", 3: "S", 4: "E"},
        "N": {0: "N", 1: "W", 2: "S", 3: "E", 4: "N"},
        "S": {0: "S", 1: "E", 2: "N", 3: "W", 4: "S"},
        "W": {0: "W", 1: "S", 2: "E", 3: "N", 4: "W"},
    }
    if instruction == "R":
        return right_mapping.get(current_direction).get(degree / 90)
    return left_mapping.get(current_direction).get(degree / 90)


interpreted = interpret_instructions(instructions)
east = interpreted.get("E")
north = interpreted.get("N")
south = interpreted.get("S")
west = interpreted.get("W")
print(f"part 1 answer is: {abs(east - west) + abs(north - south)}")

# PART 2


def interpret_instructions_in_relation_to_waypoint(
    instructions: List[str],
) -> Dict[str, int]:
    waypoint = {"E": 10, "N": 1}
    ship = {"E": 0, "N": 0, "S": 0, "W": 0}
    for instruction in instructions:
        letter = instruction[0]
        value = int(instruction[1:])
        if letter == "F":
            waypoint_direction_1, waypoint_direction_2 = list(waypoint.keys())
            waypoint_value_1 = waypoint.get(waypoint_direction_1)
            waypoint_value_2 = waypoint.get(waypoint_direction_2)
            ship[waypoint_direction_1] += value * waypoint_value_1
            ship[waypoint_direction_2] += value * waypoint_value_2
            continue
        if letter in ["L", "R"]:
            waypoint_direction_1, waypoint_direction_2 = list(waypoint.keys())
            waypoint_value_1, waypoint_value_2 = list(waypoint.values())
            new_direction_1 = _determine_direction(
                current_direction=waypoint_direction_1,
                instruction=letter,
                degree=value,
            )
            new_direction_2 = _determine_direction(
                current_direction=waypoint_direction_2,
                instruction=letter,
                degree=value,
            )
            waypoint = dict()
            waypoint[new_direction_1] = waypoint_value_1
            waypoint[new_direction_2] = waypoint_value_2
            continue
        waypoint = _update_waypoint_direction(waypoint, letter, value)
    return ship


def _update_waypoint_direction(waypoint, letter, value):
    combos = {"E": "W", "W": "E", "N": "S", "S": "N"}
    if letter in list(waypoint.keys()):
        waypoint[letter] += value
        return waypoint
    direction = combos.get(letter)
    if waypoint[direction] > value:
        waypoint[direction] -= value
        return waypoint
    new_value = value - waypoint[direction]
    waypoint[letter] = waypoint.pop(direction)
    waypoint[letter] = new_value
    return waypoint


interpreted_2 = interpret_instructions_in_relation_to_waypoint(instructions)
e = interpreted_2.get("E")
n = interpreted_2.get("N")
s = interpreted_2.get("S")
w = interpreted_2.get("W")
print(f"part 2 answer is: {abs(e - w) + abs(n - s)}")
