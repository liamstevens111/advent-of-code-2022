def solve(data):
    head_positions, tail_positions = [(0, 0)], [(0, 0)]
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0

    for line in data:
        direction, value = line.split(" ")

        for i in range(int(value)):
            match direction:
                case "U":
                    head_y += 1
                case "D":
                    head_y -= 1
                case "L":
                    head_x -= 1
                case "R":
                    head_x += 1

            head_positions.append((head_x, head_y))
            if not head_is_touching_tail(head_x, head_y, tail_x, tail_y):
                tail_x, tail_y = head_positions[-2]
                tail_positions.append(head_positions[-2])

    print(len(set(tail_positions)))


def head_is_touching_tail(head_x, head_y, tail_x, tail_y):
    return abs(head_x-tail_x) <= 1 and abs(head_y-tail_y) <= 1


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        solve(data)
