def solve(data):
    count = 0

    for line in data:
        first_elf_first_number = int(line.split(",")[0].split("-")[0])
        first_elf_second_number = int(line.split(",")[0].split("-")[1])
        second_elf_first_number = int(line.split(",")[1].split("-")[0])
        second_elf_second_number = int(line.split(",")[1].split("-")[1])

        if (first_elf_first_number >= second_elf_first_number and first_elf_second_number <= second_elf_second_number) \
                or (second_elf_first_number >= first_elf_first_number and second_elf_second_number <= first_elf_second_number):
            count += 1

    return count


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        print(solve(data))
