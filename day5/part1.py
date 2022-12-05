def solve(data):
    stacks, instructions = data.split("\n\n")
    stacks = generate_stacks(stacks.split("\n"))
    stacks = apply_instructions_to_stacks(stacks, instructions.split("\n"))

    return "".join([stack[-1] for stack in stacks])


def generate_stacks(data):
    total_stacks = int(data[-1].strip()[-1])
    stacks = [[] for i in range(total_stacks)]

    curr_stack = 0

    for line in range(len(data)-2, -1, -1):
        for column in range(1, len(data[line])-1, 4):
            if data[line][column].isalpha():
                stacks[curr_stack].append(data[line][column])
            curr_stack += 1
        curr_stack = 0

    return stacks


def apply_instructions_to_stacks(stacks, instructions):
    for instruction in instructions:
        amount_to_move, from_stack, to_stack = [
            int(val) for val in instruction.split(" ") if val.isdigit()]

        for i in range(amount_to_move):
            val = stacks[from_stack-1].pop()
            stacks[to_stack-1].append(val)

    return (stacks)


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read()
        print(solve(data))
