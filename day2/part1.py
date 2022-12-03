import os
data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

pick_score_mappings = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

result_point_mappings = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}


def solve(data):
    total_points = 0

    for line in data:
        elf_pick, player_pick = line.split(" ")

        points = result_point_mappings[elf_pick +
                                       player_pick] + pick_score_mappings[player_pick]
        total_points += points

    return total_points


if __name__ == '__main__':
    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        print(solve(data))
