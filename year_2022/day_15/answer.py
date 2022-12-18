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
