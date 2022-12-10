from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    x = 1
    cycle = 0
    indexes = [19,59,99,139,179,219]
    sum = 0
    for line in lines:
        line_arr = line.strip().split()
        if line_arr[0] == "noop":
            cycle += 1
            if cycle in indexes:
                sum += (cycle+1)*x
        else:
            cycle += 1
            if cycle in indexes:
                sum += (cycle+1)*x
            x += int(line_arr[1])
            cycle += 1
            if cycle in indexes:
                sum += (cycle+1)*x
    print(sum)

    grid = []
    for _ in range(6):
        row = []
        for __ in range(40):
            row.append(" ")
        grid.append(row)

    x = 1
    cycle = 0

    for line in lines:
        line_arr = line.strip().split()
        if line_arr[0] == "noop":
            grid = check_light(grid, cycle, x)
            cycle += 1
        else:
            grid = check_light(grid, cycle, x)
            cycle += 1
            grid = check_light(grid, cycle, x)
            cycle += 1
            x += int(line_arr[1])
    for y in range(6):
        for x in range(40):
            print(grid[y][x], end="")
        print()

def check_light(grid, cycle, x):
    y_coord = cycle // 40
    x_coord = cycle % 40
    if abs(x-x_coord) <= 1:
        grid[y_coord][x_coord] = "#"
    return grid


if __name__ == '__main__':
    main()