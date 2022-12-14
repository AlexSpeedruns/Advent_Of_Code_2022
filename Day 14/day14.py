from os.path import dirname, join

def main(part):
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = [[" "]*1000 for _ in range(200)]

    if part == 2:
        max_y = 0
        for line in lines:
            line_arr = line.strip().split(" -> ")
            for i in range(len(line_arr)):
                y = int(line_arr[i].split(",")[1])
                if y > max_y:
                    max_y = y
        floor = max_y + 2
        grid[floor] = ["#" for _ in grid[floor]]

    for line in lines:
        line_arr = line.strip().split(" -> ")
        for i in range(1, len(line_arr)):
            cur = line_arr[i].split(",")
            prev = line_arr[i-1].split(",")
            cur = [int(j) for j in cur]
            prev = [int(j) for j in prev]
            if cur[0] == prev[0] and cur[1] < prev[1]:
                grid = fill_line(grid, cur[1], prev[1], cur[0], "y")
            elif cur[0] == prev[0]:
                grid = fill_line(grid, prev[1], cur[1], cur[0], "y")
            elif cur[1] == prev[1] and cur[0] < prev[0]:
                grid = fill_line(grid, cur[0], prev[0], cur[1], "x")
            else:
                grid = fill_line(grid, prev[0], cur[0], cur[1], "x")

    start = (0,500)
    count = 0
    done = False
    while not done:
        current_sand = start
        while True:
            down_y = current_sand[0]+1
            down_x = current_sand[1]
            down_left_x = current_sand[1]-1
            down_right_x = current_sand[1]+1
            if down_y >= len(grid):
                done = True
                break
            elif grid[down_y][down_x] == " ":
                current_sand = (down_y, down_x)
                continue
            elif grid[down_y][down_left_x] == " ":
                current_sand = (down_y, down_left_x)
                continue
            elif grid[down_y][down_right_x] == " ":
                current_sand = (down_y, down_right_x)
                continue
            else:
                grid[current_sand[0]][current_sand[1]] = "o"
                count += 1
                if part == 2 and current_sand == start:
                    done = True
                break
    print(count)

def fill_line(grid, start, end, other, axis):
    if axis == "y":
        for i in range(end-start+1):
            grid[start+i][other] = "#"
    else:
        for i in range(end-start+1):
            grid[other][start+i] = "#"
    return grid

if __name__ == '__main__':
    main(1)
    main(2)