from typing import List, Union
from dataclasses import dataclass
import math
from copy import deepcopy


@dataclass
class Monkey:
    items: List[int]
    operation_type: str
    operand: Union[int, str]
    divisor: int
    throw_if_true: int
    throw_if_false: int
    number_of_items_inspected: int = 0

    def inspect_items_and_throw(self, lcm=None):
        items_to_move = []
        for item in self.items:
            self.number_of_items_inspected += 1
            if self.operand == "old":
                if self.operation_type == "m":
                    operation = item * item
            else:
                if self.operation_type == "a":
                    operation = item + self.operand
                elif self.operation_type == "m":
                    operation = item * self.operand
            if lcm:
                operation %= lcm
                if operation % self.divisor == 0:
                    items_to_move.append(
                        [self.throw_if_true, operation]
                    )
                else:
                    items_to_move.append(
                        [self.throw_if_false, operation ]
                    )
            else:
                if (operation // 3) % self.divisor == 0:
                    items_to_move.append(
                        [self.throw_if_true, operation // 3]
                    )
                else:
                    items_to_move.append(
                        [self.throw_if_false, operation // 3]
                    )
        self.items = []
        return items_to_move


monkey_zero = Monkey([62, 92, 50, 63, 62, 93, 73, 50], "m", 7, 2, 7, 1)
monkey_one = Monkey([51, 97, 74, 84, 99], "a", 3, 7, 2, 4)
monkey_two = Monkey([98, 86, 62, 76, 51, 81, 95], "a", 4, 13, 5, 4)
monkey_three = Monkey([53, 95, 50, 85, 83, 72], "a", 5, 19, 6, 0)
monkey_four = Monkey([59, 60, 63, 71], "m", 5, 11, 5, 3)
monkey_five = Monkey([92, 65], "m", "old", 5, 6, 3)
monkey_six = Monkey([78], "a", 8, 3, 0, 7)
monkey_seven = Monkey([84, 93, 54], "a", 1, 17, 2, 1)

monkeys = [
    monkey_zero,
    monkey_one,
    monkey_two,
    monkey_three,
    monkey_four,
    monkey_five,
    monkey_six,
    monkey_seven,
]


def play_rounds(monkeys: List[Monkey], rounds: int,lcm: math.lcm=None) -> None:
    for _ in range(rounds):
        for monkey in monkeys:
            items_to_move = monkey.inspect_items_and_throw(lcm=lcm)
            for id, item in items_to_move:
                monkeys[id].items.append(item)


# PART 1

copy_monkeys = deepcopy(monkeys)
play_rounds(copy_monkeys, 20)
# gets a sorted list of all inspected items by every monkey
print(sorted([item.number_of_items_inspected for item in copy_monkeys]))

# PART 2

lcm = math.lcm(*[monkey.divisor for monkey in monkeys])
play_rounds(monkeys, 10000, lcm=lcm)
# gets a sorted list of all inspected items by every monkey
print(sorted([item.number_of_items_inspected for item in monkeys]))
