from input_data import batches, valid_passport_fields
from typing import Dict, List
import re

split_batches = batches.split("\n\n")


def _parse_batch(batch: str) -> Dict[str, str]:
    lines = batch.split("\n")
    split_fields = [item.split(" ") for item in lines]
    #  unpack list of lists
    fields = [item for item in split_fields for item in item]
    parsed_batch = {item.split(":")[0]: item.split(":")[1] for item in fields}
    return parsed_batch


valid_passports = [
    batch
    for batch in split_batches
    if all(
        field in list(_parse_batch(batch=batch).keys())
        for field in valid_passport_fields
    )
]
print(f"part 1 answer: {len(valid_passports)}")


# part 2


def is_valid_year(value: str, min: int, max: int) -> bool:
    try:
        int(value)
        return min <= int(value) <= max
    except ValueError:
        return False


def is_valid_height(value: str) -> bool:
    expression_cm = r"^[0-9]{3}cm"  #  eg 123 in 123xxx
    expression_in = r"^[0-9]{2}in"  #  eg 123 in 123xxx
    if re.fullmatch(expression_cm, value):
        return 150 <= int(re.fullmatch(expression_cm, value).group(0)[:3]) <= 193
    elif re.fullmatch(expression_in, value):
        return 59 <= int(re.fullmatch(expression_in, value).group(0)[:2]) <= 76
    else:
        return False


def is_valid_hair_colour(value: str) -> bool:
    hair_colour_expression = r"\#[0-9a-f]{6}"
    if re.fullmatch(hair_colour_expression, value):
        return True
    else:
        return False


def is_valid_eye_colour(value: str) -> bool:
    valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in valid_colours


def is_valid_passport_id(value: str) -> bool:
    passport_id_expression = r"[0-9]{9}"
    if re.fullmatch(passport_id_expression, value):
        return True
    else:
        return False


def find_valid_passports(batches: List[str]) -> int:
    total_number = 0
    for batch in batches:
        parsed_batch = _parse_batch(batch)
        year_of_birth = parsed_batch.get("byr")
        year_of_issue = parsed_batch.get("iyr")
        year_of_expiry = parsed_batch.get("eyr")
        height = parsed_batch.get("hgt")
        hair_colour = parsed_batch.get("hcl")
        eye_colour = parsed_batch.get("ecl")
        passport_id = parsed_batch.get("pid")

        if (
            year_of_birth
            and year_of_issue
            and year_of_expiry
            and height
            and hair_colour
            and eye_colour
            and passport_id
            and all(
                [
                    is_valid_year(year_of_birth, 1920, 2002),
                    is_valid_year(year_of_issue, 2010, 2020),
                    is_valid_year(year_of_expiry, 2020, 2030),
                    is_valid_height(height),
                    is_valid_hair_colour(hair_colour),
                    is_valid_eye_colour(eye_colour),
                    is_valid_passport_id(passport_id),
                ]
            )
        ):
            total_number += 1

    return total_number


part_2_answer = find_valid_passports(split_batches)
print(f"part 2 answer: {part_2_answer}")
