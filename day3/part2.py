import os

from string import ascii_letters

data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

item_priority_values = dict(
    zip(ascii_letters, range(1, len(ascii_letters) + 1)))


def solve(data):
    required_count = 3

    return (sum
            ([get_priority_value_from_rucksacks(data[i:i+required_count])
              for i in range(0, len(data), required_count)]))


def get_priority_value_from_rucksacks(rucksacks):
    common_item = set(rucksacks[0]).intersection(rucksacks[1], rucksacks[2])
    return get_priority_value_from_item(common_item.pop())


def get_priority_value_from_item(item):
    return item_priority_values[item]


if __name__ == '__main__':
    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        print(solve(data))
