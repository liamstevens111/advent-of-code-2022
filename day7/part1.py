def solve(data):
    total_file_system_space = 70000000
    unused_space_requirement = 30000000

    path_sizes = {

    }

    current_path = []
    root_size = 0

    for line in data:
        values = line.split(" ")

        if values[0] == "$" and values[1] == "cd":
            if values[2] != "..":
                current_path.append(values[2])
                path_sizes["/".join(current_path)[1:]] = 0
            else:
                val = path_sizes["/".join(current_path)[1:]]
                current_path.pop()
                path_sizes["/".join(current_path)[1:]] += val
        elif values[0].isnumeric():
            if len(current_path) == 1:
                root_size += int(values[0])
            else:
                path_sizes["/".join(current_path)[1:]] += int(values[0])

    first_level_directories_size = 0

    for k, v in path_sizes.items():
        if k.count("/") == 1:
            first_level_directories_size += v

    path_sizes["/"] = root_size + first_level_directories_size

    del path_sizes[""]

    output = 0

    for k, v in path_sizes.items():
        if v <= 100000:
            output += v

    # Part 1
    print(output)

    unused_space = total_file_system_space - path_sizes["/"]
    needed_space = unused_space_requirement - unused_space

    possible_vals = []

    for v in path_sizes.values():
        if v >= needed_space:
            possible_vals.append(v)

    # Part 2
    print(min(possible_vals))


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        solve(data)
