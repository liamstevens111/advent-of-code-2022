import math


def solve(data):
    grid = [[int(y) for y in x] for x in data]

    largest = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total = math.prod(calculate_view_heights(i, j, grid))
            largest = max(total, largest)

    print(largest)


def calculate_view_heights(source_i, source_j, grid):
    calc_functions = [calc_up, calc_down, calc_left, calc_right]

    counts = [f(source_i, source_j, grid) for f in calc_functions]

    return counts


def calc_up(source_i, source_j, grid):
    count = 0
    current_i = source_i

    while current_i > 0:
        if grid[source_i][source_j] > grid[current_i-1][source_j]:
            count += 1
            current_i -= 1
        else:
            count += 1
            break

    return count or 1


def calc_down(source_i, source_j, grid):
    count = 0
    current_i = source_i

    while current_i < len(grid)-1:
        if grid[source_i][source_j] > grid[current_i+1][source_j]:
            count += 1
            current_i += 1
        else:
            count += 1
            break

    return count or 1


def calc_left(source_i, source_j, grid):
    count = 0
    current_j = source_j

    while current_j > 0:
        if grid[source_i][source_j] > grid[source_i][current_j-1]:
            count += 1
            current_j -= 1
        else:
            count += 1
            break

    return count or 1


def calc_right(source_i, source_j, grid):
    count = 0
    current_j = source_j

    while current_j < len(grid[0])-1:
        if grid[source_i][source_j] > grid[source_i][current_j+1]:
            count += 1
            current_j += 1
        else:
            count += 1
            break

    return count or 1


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        solve(data)
