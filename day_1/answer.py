from input_data import data

# make list of entries
entries = [int(item) for item in data.split("\n")]

# part 1
part_1_answer = set([x * y for y in entries for x in entries if x + y == 2020])

#  part 2
part_2_answer = set(
    [x * y * z for y in entries for x in entries for z in entries if x + y + z == 2020]
)
print(part_1_answer)
print(part_2_answer)
