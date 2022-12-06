from input_data import buffers


def get_answer(buffers: str, lenght: int) -> int:

    for index, _ in enumerate(buffers[3:], lenght):
        if len(buffers[index - lenght : index]) == len(
            set(buffers[index - lenght : index])
        ):
            return index


print(get_answer(buffers=buffers, lenght=4))
print(get_answer(buffers=buffers, lenght=14))
