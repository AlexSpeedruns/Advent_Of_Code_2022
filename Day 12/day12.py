from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = []
    for y in range(len(lines)):
        arr = []
        lines[y] = lines[y].strip()
        for x in range(len(lines[y])):
            if lines[y][x] == "S":
                start = (y,x)
                arr.append("a")
            elif lines[y][x] == "E":
                end = (y,x)
                arr.append("z")
            else:
                arr.append(lines[y][x])
        grid.append(arr)

    distance = traverse(grid, start, end)
    print(distance)

    min_dist = 99999
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if grid[y][x] == "a":
                distance = traverse(grid, (y,x), end)
                if distance is not None and distance < min_dist:
                    min_dist = distance
    print(min_dist)

def traverse(grid, start, end):
    valid_options = []
    valid_options.append((start, 0))
    seen_options = set()
    while len(valid_options) > 0:
        current_pos, current_dist = valid_options.pop(0)
        if current_pos == end:
            return current_dist
        elif current_pos in seen_options:
            continue
        seen_options.add(current_pos)
        current_value = ord(grid[current_pos[0]][current_pos[1]])
        if current_pos[0] > 0 and ord(grid[current_pos[0]-1][current_pos[1]]) - current_value <= 1:
            valid_options.append(((current_pos[0]-1,current_pos[1]), current_dist + 1))
        if current_pos[0] < len(grid)-1 and ord(grid[current_pos[0]+1][current_pos[1]]) - current_value <= 1:
            valid_options.append(((current_pos[0]+1,current_pos[1]), current_dist + 1))
        if current_pos[1] > 0 and ord(grid[current_pos[0]][current_pos[1]-1]) - current_value <= 1:
            valid_options.append(((current_pos[0],current_pos[1]-1), current_dist + 1))
        if current_pos[1] < len(grid[0])-1 and ord(grid[current_pos[0]][current_pos[1]+1]) - current_value <= 1:
            valid_options.append(((current_pos[0],current_pos[1]+1), current_dist + 1))
    return None

if __name__ == '__main__':
    main()