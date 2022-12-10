def solve(data):
    print(do_solve(data, 2))  # Part 1
    print(do_solve(data, 10))  # Part 2


def do_solve(data, total_knots):
    knot_position_histories = [[(0, 0)] for i in range(total_knots)]
    knot_current_positions = [[0, 0] for i in range(total_knots)]

    for line in data:
        direction, value = line.split(" ")

        for i in range(int(value)):
            match direction:
                case "U":
                    knot_current_positions[-1][1] += 1
                case "D":
                    knot_current_positions[-1][1] -= 1
                case "L":
                    knot_current_positions[-1][0] -= 1
                case "R":
                    knot_current_positions[-1][0] += 1

            knot_position_histories[-1].append(
                tuple(knot_current_positions[-1]))

            for knot_index in range(len(knot_current_positions)-2, -1, -1):
                if not knot_is_touching_other(knot_current_positions[knot_index+1], knot_current_positions[knot_index]):
                    if knot_current_positions[knot_index+1][0] > knot_current_positions[knot_index][0]:
                        knot_current_positions[knot_index][0] += 1
                    elif knot_current_positions[knot_index+1][0] < knot_current_positions[knot_index][0]:
                        knot_current_positions[knot_index][0] -= 1

                    if knot_current_positions[knot_index+1][1] > knot_current_positions[knot_index][1]:
                        knot_current_positions[knot_index][1] += 1
                    elif knot_current_positions[knot_index+1][1] < knot_current_positions[knot_index][1]:
                        knot_current_positions[knot_index][1] -= 1

                    knot_position_histories[knot_index].append(
                        tuple(knot_current_positions[knot_index]))

    return (len(set(knot_position_histories[0])))


def knot_is_touching_other(first_knot, second_knot):
    return abs(first_knot[0]-second_knot[0]
               ) <= 1 and abs(first_knot[1]-second_knot[1]) <= 1


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read().splitlines()
        solve(data)
