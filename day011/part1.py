import math


def solve(data):
    monkey_data = parse_data(data)

    for i in range(20):
        for current_monkey in monkey_data.keys():
            while monkey_data[current_monkey]["items"]:
                monkey_data[current_monkey]["inspections"] += 1

                item_to_throw = monkey_data[current_monkey]["items"].pop(0)
                operands = monkey_data[current_monkey]["calculations"]

                if operands[0] == "*":
                    item_to_throw *= int(operands[1]) if len(
                        operands) == 2 else int(item_to_throw)
                elif operands[0] == "+":
                    item_to_throw += int(operands[1]) if len(
                        operands) == 2 else int(item_to_throw)
                elif operands[0] == "-":
                    item_to_throw -= int(operands[1]) if len(
                        operands) == 2 else int(item_to_throw)
                elif operands[0] == "/":
                    item_to_throw //= int(operands[1]) if len(
                        operands) == 2 else int(item_to_throw)

                item_to_throw = item_to_throw // 3

                to_monkey = monkey_data[current_monkey]["tests"][
                    1] if item_to_throw % monkey_data[current_monkey]["tests"][
                        0] == 0 else monkey_data[current_monkey]["tests"][2]

                monkey_data[to_monkey]["items"].append(item_to_throw)

    total = math.prod(
        sorted([
            inspection_count for inspection_count in [
                monkey_stats["inspections"]
                for monkey_stats in monkey_data.values()
            ]
        ])[-1:-3:-1])

    print(total)


def parse_data(data):
    parsed_monkey_data = {}

    monkey_data = data.split("Monkey")
    for monkey_line in monkey_data[1:]:
        monkey_index, monkey_stats = parse_monkey_from_line(
            monkey_line.strip().split("\n"))
        parsed_monkey_data[monkey_index] = monkey_stats

    return parsed_monkey_data


def parse_monkey_from_line(line):
    monkey_index = int(line[0][0])
    monkey_stats = {}

    monkey_stats["items"] = [
        int(item) for item in line[1].split(':')[1].strip().split(",")
    ]

    monkey_stats["calculations"] = line[2].split("old")[1].strip().split(" ")

    monkey_stats["tests"] = [
        int(n) for n in [line[i].split(" ")[-1] for i in range(3, 6)]
    ]

    monkey_stats["to_monkeys"] = []

    monkey_stats["inspections"] = 0

    return monkey_index, monkey_stats


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read()
        solve(data)
