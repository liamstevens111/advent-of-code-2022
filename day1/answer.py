import os
data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")


def solve(data):
    # First question
    print(total_calories_from_top_elf(data))

    # Second question
    print(total_calories_from_top_elf(data, 3))


def total_calories_from_top_elf(data, elf_count=1):
    return sum(data[:elf_count])


def transform(data):
    transformed_data = []
    curr = 0

    for line in data:
        if len(line.strip()) == 0:
            transformed_data.append(curr)
            curr = 0
        else:
            curr += int(line)

    return sorted(transformed_data, reverse=True)


if __name__ == '__main__':
    with open(data_file_path, 'r') as file:
        data = file.readlines()
        data = transform(data)
        solve(data)
