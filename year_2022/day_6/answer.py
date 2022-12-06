from input_data import buffers


def get_answer(buffers: str, length: int) -> int:

    for index, _ in enumerate(buffers[3:], length):
        if len(buffers[index - length : index]) == len(
            set(buffers[index - length : index])
        ):
            return index


print(get_answer(buffers=buffers, length=4))
print(get_answer(buffers=buffers, length=14))
