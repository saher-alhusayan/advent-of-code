from input_data import instructions as d
from typing import Dict, List, Any
import re

data = d.split("$ ")


def get_sub_dirs(string: str) -> List[str]:
    ls = []
    dirs = string.split("/")
    directories = [item for item in dirs if item != "root" and item != ""]
    for i in range(0, len(directories)):
        ls.append("root/" + "/".join(directories) + "/")
        directories.pop(-1)
    return ls


def get_total_disk_space(instructions: List[str]) -> int:
    total = 0
    for line in instructions:
        for item in line.split("\n"):
            if bool(re.search(r"\d", item)):
                total += int(item.split(" ")[0])
    return total


def action_commands(instructions: List[str]) -> Dict[str, Any]:
    filesystem = {"root/": {}}
    path = "root/"
    for _, line in enumerate(instructions):
        if "ls" in line:
            for item in line.split("\n"):
                if "dir" in item:
                    new_dir_path = path + item.split(" ")[1] + "/"
                    filesystem[new_dir_path] = {}
                if bool(re.search(r"\d", item)):
                    filesystem[path].update(
                        {path + item.split(" ")[1]: int(item.split(" ")[0])}
                    )
                    if path != "root/":
                        paths = get_sub_dirs(path)
                        for new_path in paths:
                            try:
                                filesystem[new_path].update(
                                    {path + item.split(" ")[1]: int(item.split(" ")[0])}
                                )
                            except KeyError:
                                pass
        if "cd .." in line:
            if path != "root/":
                path = "/".join(path.split("/")[:-2]) + "/"

        if bool(re.search(r"cd [a-zA-Z]", line)):
            path = path + line.split("\n")[0].split(" ")[1] + "/"
    return filesystem


part_1_answer = action_commands(data)

sums_of_dirs = [
    sum(item.values()) for item in part_1_answer.values() if sum(item.values()) < 100000
]

print(sum(sums_of_dirs))


# PART 2


target = 30000000 - (70000000 - get_total_disk_space(data))

valid_directories_to_remove = [
    sum(item.values()) for item in part_1_answer.values() if sum(item.values()) > target
]

print(min(valid_directories_to_remove))
