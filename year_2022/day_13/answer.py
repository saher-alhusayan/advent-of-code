from input_data import pairs as data 
from typing import List, Any
import json 

class RightOrder(Exception):
    pass

class WrongOrder(Exception):
    pass


pairs = data.split('\n\n')
pairs = [item.split('\n') for item in pairs]

def get_answer(pairs:List[List[str]]) -> int:
    total = 0
    for index, pair in enumerate(pairs, 1):
        list1, list2 = pair
        ls1 = json.loads(list1)
        ls2 = json.loads(list2)
        try:
            in_the_right_order(ls1, ls2)
        except WrongOrder:
            continue
        except RightOrder:
            total += index
    return total

def in_the_right_order(pair1: List[Any], pair2: List[Any]) -> None:
        if not pair1 and pair2:
            raise RightOrder

        if isinstance(pair1, int) and isinstance(pair2, int) and pair1 > pair2:
            raise WrongOrder
        if isinstance(pair1, int) and isinstance(pair2, int) and pair1 < pair2:
            raise RightOrder
        if isinstance(pair1, int) and isinstance(pair2, list):
            in_the_right_order([pair1], pair2) 
        if isinstance(pair2, int) and isinstance(pair1, list):
            in_the_right_order(pair1, [pair2])
        if isinstance(pair1, list) and isinstance(pair2, list):
            for val in zip(pair1, pair2): 
                if val[0] == val[1]:
                    continue 
                in_the_right_order(val[0], val[1])
            if len(pair1) <= len(pair2):
                raise RightOrder
            else:
                raise WrongOrder


print(get_answer(pairs))

