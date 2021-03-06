from typing import Any, Dict, List

from input_data import data


def make_data_dictionaries(lines: List[str]) -> List[Dict[str, Any]]:
    dictionaries: List[Dict[str, Any]] = []
    for line in lines:
        min_occurance = int(line.split("-")[0])
        max_occurance = int(line.split(" ")[0].split("-")[1])
        letter = line.split(" ")[1][0]
        password = line.split(" ")[2]
        dictionaries.append(
            {
                "min_occurance": min_occurance,
                "max_occurance": max_occurance,
                "letter": letter,
                "password": password,
            }
        )
    return dictionaries


def does_password_conform_to_policy(policy_and_password: Dict[str, Any]) -> bool:
    min_occurance = policy_and_password.get("min_occurance")
    max_occurance = policy_and_password.get("max_occurance")
    letter = policy_and_password.get("letter")
    password = policy_and_password.get("password")
    if min_occurance <= password.count(letter) <= max_occurance:
        return True
    else:
        return False


policies_and_passwords = make_data_dictionaries(data.split("\n"))
part_1_answer = len(
    [
        dictionary
        for dictionary in policies_and_passwords
        if does_password_conform_to_policy(dictionary)
    ]
)
print(part_1_answer)


def check_letter_in_two_positions(policy_and_password: Dict[str, Any]) -> bool:
    position_one = policy_and_password.get("min_occurance")
    position_two = policy_and_password.get("max_occurance")
    letter = policy_and_password.get("letter")
    password = policy_and_password.get("password")
    index_one = position_one - 1
    index_two = position_two - 1
    if (password[index_one] == letter and password[index_two] != letter) or (
        password[index_one] != letter and password[index_two] == letter
    ):
        return True
    else:
        return False


part_2_answer = len(
    [
        dictionary
        for dictionary in policies_and_passwords
        if check_letter_in_two_positions(dictionary)
    ]
)
print(part_2_answer)
