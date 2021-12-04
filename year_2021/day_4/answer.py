from input_data import data
from typing import Tuple, Set, List

# PREPPING DATA #
numbers = data.split("\n")[0].split(",")
numbers = [int(n) for n in numbers]
boards = data.split("\n\n")[1:]

# PART 1 #


def _parse_board(board: str) -> Tuple[List[Tuple[int]], List[Tuple[int]]]:
    rows = board.split("\n")
    split_rows = [row.split(" ") for row in rows]
    formatted_rows = _format_rows(split_rows)
    columns = list(zip(*formatted_rows))
    return formatted_rows, columns


def _format_rows(rows: List[List[str]]) -> List[Tuple[int]]:
    formatted_rows: List[Set[int]] = []
    for row in rows:
        row = [int(item) for item in row if item != ""]
        formatted_rows.append(tuple(row))
    return formatted_rows


def _calculate_scores(boards: List[str], numbers: List[int]) -> List[int]:
    all_sums: List[int] = []
    numbers_called: List[int] = []
    already_won: List[int] = []
    for number in numbers:
        numbers_called.append(number)
        for index, board in enumerate(boards):
            rows, columns = _parse_board(board)
            if index not in already_won:
                if any(set(row).issubset(set(numbers_called)) for row in rows) or any(
                    set(column).issubset(set(numbers_called)) for column in columns
                ):
                    already_won.append(index)
                    numbers_to_sum = _get_uncalled_numbers(rows, set(numbers_called))
                    all_sums.append(sum(numbers_to_sum) * number)

    return all_sums


def _get_uncalled_numbers(
    rows: List[Tuple[int]], numbers_called: Set[int]
) -> List[int]:
    all_uncalled: List[int] = []
    for row in rows:
        uncalled = set(row).difference(numbers_called)
        all_uncalled += [*uncalled]
    return list(set(all_uncalled))


all_scores = _calculate_scores(boards, numbers)
print(f"answer to part 1: {all_scores[0]}")
print(f"answer to part 2: {all_scores[-1]}")
