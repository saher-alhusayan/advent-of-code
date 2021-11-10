import input_data

# Make data #
d = input_data.sequence.split("\n")
data = [line.split(" ") for line in d]

data = [[lst[0], lst[1][1:], lst[1][0]] for lst in data]
print(data[:3])
# PART 1 #


def rules(number, data, indexes, current_index):
    if current_index in indexes:
        raise ValueError(f"instruction with index {current_index} run before")

    instruction, value, operation = data[current_index]
    value = int(value)
    if instruction == "nop":
        indexes.append(current_index)
        current_index += 1
    if instruction == "acc":
        indexes.append(current_index)
        current_index += 1
        if operation == "+":
            number += value
        else:
            number -= value
    if instruction == "jmp":
        indexes.append(current_index)
        if operation == "+":
            current_index = current_index + value
        else:
            current_index = current_index - value

    return number, current_index


def get_number(data):
    number = 0
    indexes = []
    index = 0
    try:
        while True:
            number, index = rules(number, data, indexes, index)

    except ValueError:
        return number, indexes
    return number


total, _ = get_number(data)
print(f"part 1 answer is {total}")


# PART 2 #


def get_number_part_2(data):
    number = 0
    indexes = []
    index = 0

    while index <= len(data) - 1:
        try:
            number, index = rules(number, data, indexes, index)

        except ValueError:
            raise

    return number


def change_instruction(instruction):
    if instruction == "nop":
        instruction = "jmp"
        return instruction
    if instruction == "jmp":
        instruction = "nop"
        return instruction
    else:
        return instruction


for index, _ in enumerate(data):
    data[index][0] = change_instruction(data[index][0])

    try:
        number = get_number_part_2(data)
        break
    except ValueError:
        data[index][0] = change_instruction(data[index][0])

        continue

print(f"part 2 answer is {number}")
