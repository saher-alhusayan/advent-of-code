from typing import Dict

import rules

REQUIRED_BAG = "shiny gold"
# make data #


def _sort_out_bags(lst):
    values = {}
    for bag_type in lst:
        try:
            int(bag_type[0])
        except ValueError:
            return {}
        value, _ = bag_type.split(" bag")
        num = value[0]
        bag_colour = value[2:]

        d = {bag_colour: int(num)}
        values.update(d)
    return values


def make_dict_out_of_rules(combinations: str) -> Dict[str, Dict[str, int]]:
    rules = combinations.split("\n")
    data = {}
    for rule in rules:
        bag, contained_bags = rule.split(" bags contain ")
        all_containged_bags = contained_bags.split(", ")
        values = _sort_out_bags(all_containged_bags)
        d = {bag: values}
        data.update(d)
    return data


# PART 1 #


def get_list_of_bags_that_can_conatin_others(data, required_list):
    lst_of_bags = []
    for bag in required_list:
        bags_that_contain_it = find_bags_containing_specified_bag(data, bag)
        lst_of_bags.append(bags_that_contain_it)
    return [bag for lst in lst_of_bags for bag in lst]


def find_bags_containing_specified_bag(data, item):
    bags = [key for key, value in data.items() if item in value.keys()]
    return bags


def calculate_number_of_possible_bags(required_bag, data):
    bags_directly_containing_required = [
        key for key, value in data.items() if required_bag in value.keys()
    ]
    total_bags = []
    direct_bags = bags_directly_containing_required
    while len(bags_directly_containing_required) > 0:
        bags = get_list_of_bags_that_can_conatin_others(
            data, bags_directly_containing_required
        )
        total_bags.append(list(set(bags)))
        bags_directly_containing_required = list(set(bags))

    unpacked_total_bags = [bag for lst in total_bags for bag in lst]

    total = set(direct_bags) | set(unpacked_total_bags)
    return len(total)


data = make_dict_out_of_rules(rules.combos)
total = calculate_number_of_possible_bags(required_bag=REQUIRED_BAG, data=data)

print(total)


# PART 2 #


def get_number_of_bags(bags_within, data, number=0, mltplr=1):
    for bag, multiplier in bags_within.items():
        bgs = data.get(bag)
        if bgs:
            new_multiplier = multiplier * mltplr
            number += new_multiplier
            number = get_number_of_bags(bgs, data, number, new_multiplier)

        else:
            number += mltplr * multiplier

    return number


within = data.get(REQUIRED_BAG)
result = get_number_of_bags(within, data)
print(result)
