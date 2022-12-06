def solve(data, unique_length):
    last_characters = []
    last_characters.extend(data[0:unique_length])

    if len(set(last_characters)) == unique_length:
        return last_characters

    for i in range(unique_length, len(data)):
        last_characters.pop(0)
        last_characters.append(data[i])

        if len(set(last_characters)) == unique_length:
            return i+1


if __name__ == '__main__':
    import os
    data_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(data_file_path, 'r') as file:
        data = file.read()
        print(solve(data, 4))
        print(solve(data, 14))
