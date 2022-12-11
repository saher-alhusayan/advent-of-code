from typing import List, Union
from dataclasses import dataclass


@dataclass
class Monkey:
    items: List[int]
    operation_type: str
    operand: Union[int, str]
    divisor: int
    throw_if_true: int
    throw_if_false: int
    number_of_items_inspected: int = 0

    def inspect_items_and_throw(self, worry_level_divisor):
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
            if (operation // worry_level_divisor) % self.divisor == 0:
                items_to_move.append(
                    [self.throw_if_true, operation // worry_level_divisor]
                )
            else:
                items_to_move.append(
                    [self.throw_if_false, operation // worry_level_divisor]
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


def play_round(monkeys: List[Monkey], rounds: int, worry_level_divisor) -> None:
    for _ in range(rounds):
        for monkey in monkeys:
            items_to_move = monkey.inspect_items_and_throw(worry_level_divisor)
            # print(monkey.number_of_items_inspected)
            for id, item in items_to_move:
                monkeys[id].items.append(item)


play_round(monkeys, 20, 3)
# gets a sorted list of all inspected items by every monkey
print(sorted([item.number_of_items_inspected for item in monkeys]))
