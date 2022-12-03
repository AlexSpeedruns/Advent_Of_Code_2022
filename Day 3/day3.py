from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    part1(lines)
    part2(lines)

def part1(lines):
    sum = 0
    for line in lines:
        half = len(line.strip())/2
        first = set(line[0:int(half)])
        second = set(line[int(half):])
        common = first.intersection(second)
        for char in common:
            sum += calculate_value(char)
    print(sum)

def part2(lines):
    sum = 0
    for i in range(2, len(lines), 3):
        first = set(lines[i-2].strip())
        second = set(lines[i-1].strip())
        third = set(lines[i].strip())
        common = set.intersection(first, second, third)
        for char in common:
            sum += calculate_value(char)
    print(sum)

def calculate_value(common):
    if ord(common) <= 90:
        return ord(common) - 38
    else:
        return ord(common) - 96

if __name__ == '__main__':
    main()