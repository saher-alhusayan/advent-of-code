from input_data import moves
from typing import List, Dict
import re

crates = {
    1: ["S", "C", "V", "N"],
    2: ["Z", "M", "J", "H", "N", "S"],
    3: ["M", "C", "T", "G", "J", "N", "D"],
    4: ["T", "D", "F", "J", "W", "R", "M"],
    5: ["P", "F", "H"],
    6: ["C", "T", "Z", "H", "J"],
    7: ["D", "P", "R", "Q", "F", "S", "L", "Z"],
    8: ["C", "S", "L", "H", "D", "F", "P", "W"],
    9: ["D", "S", "M", "P", "F", "N", "G", "Z"],
}
instructs = moves.split("\n")
instructions = [re.findall(r"\d+", item) for item in instructs]


def action_moves(
    crates: Dict[int, List[str]], instructions: List[List[str]]
) -> Dict[int, List[str]]:
    for instruction in instructions:
        number_of_crates_to_move, crate_from, crate_to = instruction
        stack_from = crates.get(int(crate_from))
        stack_to = crates.get(int(crate_to))
        stacks_to_move = stack_from[-int(number_of_crates_to_move) :]
        stacks_to_move.reverse()
        for stack in stacks_to_move:
            stack_to.append(stack)
        for stack in stacks_to_move:
            stack_from.pop(-1)


action_moves(crates=crates, instructions=instructions)
print([v[-1:] for v in crates.values()])
