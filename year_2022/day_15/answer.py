from input_data import sensors_and_beacons as data
import re
from typing import List, Tuple
import functools

# PART 1

TARGET = 2000000


def prep_data(sensors_and_beacons: str) -> List[List[Tuple[int, int]]]:
    all = []
    s_and_b = sensors_and_beacons.split("\n")
    for pair in s_and_b:
        x_r = "x=-?\d+"
        y_r = "y=-?\d+"
        xs = re.findall(x_r, pair)
        ys = re.findall(y_r, pair)
        if len(xs) == 1:
            xs = xs * 2
        if len(ys) == 1:
            ys = ys * 2
        all.append(
            [
                (int(xs[0].split("=")[1]), int(ys[0].split("=")[1])),
                (int(xs[1].split("=")[1]), int(ys[1].split("=")[1])),
            ]
        )
    return all


def calculate_manhatan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_points_where_beacon_cant_be(
    sensor_beacon: List[Tuple[int, int]], target: int
) -> List[List[int]]:
    all = []
    sensor, beacon = sensor_beacon
    m_dis = calculate_manhatan_distance(sensor, beacon)
    distance_to_sensor = abs(target - sensor[1])
    left = sensor[0] - (m_dis - distance_to_sensor)
    right = sensor[0] + (m_dis - distance_to_sensor)
    rng = list(range(left, right + 1))
    all.append(rng)
    return all


ls = prep_data(data)

all_blocked_points = map(
    functools.partial(get_points_where_beacon_cant_be, target=TARGET), ls
)
unpack = [item for x in all_blocked_points for item in x]
print(len(set([item for x in unpack for item in x if item != TARGET])))


# PART 2


def get_sensor_edges(
    sensors_beacons: List[List[Tuple[int, int]]]
) -> Tuple[List[int], List[int]]:
    negative = []
    positive = []
    for sensor_beacon in sensors_beacons:
        sensor, beacon = sensor_beacon
        m_dist = calculate_manhatan_distance(sensor, beacon)
        positive.append(sensor[0] - sensor[1] - m_dist)
        positive.append(sensor[0] - sensor[1] + m_dist)
        negative.append(sensor[0] + sensor[1] - m_dist)
        negative.append(sensor[0] + sensor[1] + m_dist)
    return positive, negative


def find_distress_beacon(lines: List[int]) -> int:
    for _, item in enumerate(lines):
        for _, item2 in enumerate(lines, 1):
            if abs(item - item2) == 2:
                return min(item, item2) + 1


positive, negative = get_sensor_edges(ls)
pos = find_distress_beacon(positive)
neg = find_distress_beacon(negative)

distress_beacon_x = (pos + neg) // 2
distress_beacon_y = (neg - pos) // 2
answer = (4000000 * distress_beacon_x) + distress_beacon_y
print(answer)
