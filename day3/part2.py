import os

from string import ascii_letters

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

item_priority_values = dict(
    zip(ascii_letters, range(1, len(ascii_letters) + 1)))


def solve(data):
    total = 0

    required_rucksacks = 3
    current_rucksack = 0
    rucksacks = []

    for rucksack in data:
        rucksacks.append(rucksack)
        current_rucksack += 1

        if current_rucksack == required_rucksacks:
            total += get_priority_value_from_rucksacks(rucksacks)
            current_rucksack = 0
            rucksacks.clear()

    return total


def get_priority_value_from_rucksacks(rucksacks):
    common_item = set(rucksacks[0]).intersection(rucksacks[1], rucksacks[2])
    return get_priority_value_from_item(common_item.pop())


def get_priority_value_from_item(item):
    return item_priority_values[item]


if __name__ == '__main__':
    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        print(solve(data))
