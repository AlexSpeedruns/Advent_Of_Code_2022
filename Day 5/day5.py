from os.path import dirname, join
import copy

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()
    input = parse(lines)
    part1(copy.deepcopy(input), lines)
    print()
    part2(input, lines)

def part1(input, lines):
    for i in range(10, len(lines)):
        line = lines[i]
        line_arr = line.split(" ")
        amount = int(line_arr[1])
        start = int(line_arr[3])-1
        end = int(line_arr[5])-1
        for _ in range(amount):
            value = input[start].pop()
            input[end].append(value)

    for l in input:
        print(l[-1], end="")

def part2(input, lines):
    for i in range(10, len(lines)):
        line = lines[i]
        line_arr = line.split(" ")
        amount = int(line_arr[1])
        start = int(line_arr[3])-1
        end = int(line_arr[5])-1
        for j in range(amount*-1, 0, 1):
            value = input[start][j]
            input[end].append(value)
            del input[start][j]

    for l in input:
        print(l[-1], end="")

def parse(lines):
    input = []
    for i in range(9):
        arr = []
        for j in range(7, -1, -1):
            line = lines[j]
            line_arr = [char for char in line]
            index = 1+(4*i)
            if line_arr[index] != " ":
                arr.append(line_arr[index])
        input.append(arr)
    return input

if __name__ == '__main__':
    main()