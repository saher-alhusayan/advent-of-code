from input_data import data
from typing import List, Tuple, Optional
from itertools import zip_longest
from collections import Counter

coordindates = data.split("\n")
lines = [item.split("->") for item in coordindates]


def _format_data(lines: List[List[str]]) -> List[List[Tuple[int]]]:
    coordindates: List[Tuple[int]] = []
    for line in lines:
        point_one = line[0]
        point_two = line[1]
        x1, y1 = (int(n) for n in point_one.split(","))
        x2, y2 = (int(n) for n in point_two.split(","))
        coordindates.append([(x1, y1), (x2, y2)])
    return coordindates


def _get_points_covered_between_two_points(
    point_one: Tuple[int], point_two: Tuple[int]
) -> List[Optional[Tuple[int]]]:
    x1, y1 = point_one
    x2, y2 = point_two
    if x1 == x2:
        r = range(sorted([y1, y2])[0] + 1, sorted([y1, y2])[1])
        points = zip_longest([x1], list(r), fillvalue=x1)
        return list(points) + [point_one, point_two]

    if y1 == y2:
        r = range(sorted([x1, x2])[0] + 1, sorted([x1, x2])[1])
        points = zip_longest(list(r), [y1], fillvalue=y1)
        return list(points) + [point_one, point_two]

    # else: # uncomment for answer to part 1
    #     return []

    # next two statements are for answer 2. To get answer to part 1 comment out
    # the below statements and uncomment the above two lines
    elif x1 == y1 and x2 == y2:
        r = range(sorted([y1, y2])[0] + 1, sorted([y1, y2])[1])
        points = zip(list(r), list(r))
        return list(points) + [point_one, point_two]

    else:
        r = range(sorted([x1, x2])[0] + 1, sorted([x1, x2])[1])
        points = _calculate_points(x1, y1, x2, y2)
        points_ = points + [point_one, point_two]

        return list(set(points_))


# Not happy at all with this function. Need to find a better (smarter) way
def _calculate_points(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int]]:
    lst = []
    r1 = list(range(x1, x2))
    r2 = list(range(y1, y2))
    if not r1 and r2:
        lst.append(
            list(
                zip(
                    sorted(list(range(x2 + 1, x1)), reverse=True),
                    list(range(y1 + 1, y2)),
                )
            )
        )
    if not r2 and r1:
        lst.append(
            list(
                zip(
                    list(range(x1 + 1, x2)),
                    sorted(list(range(y2 + 1, y1)), reverse=True),
                )
            )
        )
    if r1 and r2:
        lst.append(list(zip(r1, r2)))

    if not r1 and not r2:
        lst.append(
            list(
                zip(
                    sorted(list(range(x2 + 1, x1)), reverse=True),
                    sorted(list(range(y2 + 1, y1)), reverse=True),
                )
            )
        )

    return [x for item in lst for x in item]


def _calculate_answer(lines: List[List[str]]) -> int:
    points: List[Tuple[int]] = []
    coordindates = _format_data(lines)
    for coordinate in coordindates:
        point_one = coordinate[0]
        point_two = coordinate[1]
        covered_points = _get_points_covered_between_two_points(point_one, point_two)
        points.append(list(set(covered_points)))
    unpacked_points = [t for lst in points for t in lst]
    return len([item for item in Counter(unpacked_points).most_common() if item[1] > 1])


part_1_answer = _calculate_answer(lines)
print(f"answer to part 1: {part_1_answer}")
