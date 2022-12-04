def solve(data):
    count = 0

    for line in data:
        first_elf_first_number = line.split(",")[0].split("-")[0]
        first_elf_second_number = line.split(",")[0].split("-")[1]
        second_elf_first_number = line.split(",")[1].split("-")[0]
        second_elf_second_number = line.split(",")[1].split("-")[1]

        first_elf_numbers = set([i for i in range(
            int(first_elf_first_number), int(first_elf_second_number) + 1)])

        second_elf_numbers = set([i for i in range(
            int(second_elf_first_number), int(second_elf_second_number) + 1)])

        count += 1 if first_elf_numbers & second_elf_numbers else 0

    return count


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        print(solve(data))
