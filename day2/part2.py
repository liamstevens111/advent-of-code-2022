import os
data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

result_point_mappings = {
    'AX': 3,
    'AY': 4,
    'AZ': 8,
    'BX': 1,
    'BY': 5,
    'BZ': 9,
    'CX': 2,
    'CY': 6,
    'CZ': 7
}


def solve(data):
    total_points = 0

    for line in data:
        elf_pick, desired_result = line.split(" ")

        total_points += result_point_mappings[elf_pick + desired_result]

    return total_points


if __name__ == '__main__':
    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        print(solve(data))
