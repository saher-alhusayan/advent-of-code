from input_data import pairs as data 
from typing import List, Any
import json 


pairs = data.split('\n\n')
pairs = [item.split('\n') for item in pairs]


def get_answer(pairs:List[List[str]]) -> int:
    total = 0
    for index, pair in enumerate(pairs, 1):
        list1, list2 = pair
        ls1 = json.loads(list1)
        ls2 = json.loads(list2)
        outcome =  in_the_right_order(ls1, ls2)
        if outcome:
            total += index
        if outcome is None:
            print(outcome)
    return total

def in_the_right_order(pair1: List[Any], pair2: List[Any]) -> None:
    
        if isinstance(pair1, int) and isinstance(pair2, int) and pair1 > pair2:
            return False
        if isinstance(pair1, int) and isinstance(pair2, int) and pair1 < pair2:
            return True
        if isinstance(pair1, int) and isinstance(pair2, list):
            return in_the_right_order([pair1], pair2) 
        if isinstance(pair2, int) and isinstance(pair1, list):
            return in_the_right_order(pair1, [pair2])
        if isinstance(pair1, list) and isinstance(pair2, list):
            for val in zip(pair1, pair2): 
                if val[0] == val[1]:
                    continue 
                return in_the_right_order(val[0], val[1])
            return len(pair1) < len(pair2)
      

print(get_answer(pairs))

# PART 2

def sort_pairs(pairs, divider):
    sorted_pairs = []
    for pair in pairs:
        if in_the_right_order(pair, divider) is True:
            sorted_pairs.append(pair)
     
    return len(sorted_pairs)

all_pairs = []
for pair in pairs:
    list1, list2 = pair
    ls1 = json.loads(list1)
    ls2 = json.loads(list2)
    all_pairs.append(ls1)
    all_pairs.append(ls2)


sorted_pairs_1 = sort_pairs(all_pairs, [[2]])
sorted_pairs_2 = sort_pairs(all_pairs, [[6]])

answer = (sorted_pairs_1 + 1) * (sorted_pairs_2 + 2)
print(answer)
