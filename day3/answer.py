import os

from string import ascii_letters

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

item_priority_values = dict(
    zip(ascii_letters, range(1, len(ascii_letters) + 1)))


def solve(data):
    return (sum([get_priority_value_from_rucksack(rucksack)
                 for rucksack in data]))


def get_priority_value_from_rucksack(rucksack):
    sack_total_value = 0

    compartments = get_compartments_from_rucksack(rucksack)
    common_items = set(compartments[0]).intersection(compartments[1])

    while common_items:
        item = common_items.pop()
        sack_total_value += get_priority_value_from_item(item)

    return sack_total_value


def get_compartments_from_rucksack(rucksack):
    middle = len(rucksack)//2
    return (rucksack[:middle], rucksack[middle:])


def get_priority_value_from_item(item):
    return item_priority_values[item]


if __name__ == '__main__':
    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        print(solve(data))
