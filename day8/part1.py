def solve(data):
    grid = [[int(y) for y in x] for x in data]

    result_grid = [[0 for y in x] for x in data]

    outside_visible_trees = (len(grid[0]) * 2) + ((len(grid)-2)*2)

    for i in range(1, len(grid[0])-1):
        for j in range(1, len(grid)-1):
            if grid[i][j] > max(grid[i][j-1::-1]):
                result_grid[i][j] = 1
        for k in range(len(grid)-2, 0, -1):
            if grid[i][k] > max(grid[i][k+1:]):
                result_grid[i][k] = 1

    for i in range(1, len(grid[0])-1):
        for j in range(1, len(grid)-1):
            if grid[j][i] > max([grid[j][i] for j in range(j-1, -1, -1)]):
                result_grid[j][i] = 1
        for k in range(len(grid)-2, 0, -1):
            if grid[k][i] > max([grid[k][i] for k in range(k+1, len(grid))]):
                result_grid[k][i] = 1

    inside_visible_trees = 0

    for i in range(len(result_grid)):
        for j in range(len(result_grid[0])):
            inside_visible_trees += result_grid[i][j]

    total = outside_visible_trees + inside_visible_trees

    print(total)


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        solve(data)
