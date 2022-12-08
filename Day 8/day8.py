from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = []
    for line in lines:
        row = []
        for num in line.strip():
            row.append(int(num))
        grid.append(row)

    count = 0
    max_score = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_visible(grid, x, y):
                count += 1
            score = get_score(grid, x, y)
            if score > max_score:
                max_score = score
    print(count)
    print(max_score)

def is_visible(grid, x, y):
    current = grid[x][y]
    visible = 4
    if y > 0:
        for i in range(y-1, -1, -1):
            if grid[x][i] >= current:
                visible -= 1
                break
    if y < 98:
        for i in range(y+1, 99):
            if grid[x][i] >= current:
                visible -= 1
                break
    if x > 0:
        for i in range(x-1, -1, -1):
            if grid[i][y] >= current:
                visible -= 1
                break
    if x < 98:
        for i in range(x+1, 99):
            if grid[i][y] >= current:
                visible -= 1
                break
    return visible

def get_score(grid, x, y):
    current = grid[x][y]
    if y > 0:
        one = 0
        for i in range(y-1, -1, -1):
            one += 1
            if grid[x][i] >= current:
                break
    else:
        return 0
    if y < 98:
        two = 0
        for i in range(y+1, 99):
            two += 1
            if grid[x][i] >= current:
                break
    else:
        return 0
    if x > 0:
        three = 0
        for i in range(x-1, -1, -1):
            three += 1
            if grid[i][y] >= current:
                break
    else:
        return 0
    if x < 98:
        four = 0
        for i in range(x+1, 99):
            four += 1
            if grid[i][y] >= current:
                break
    else:
        return 0
    return one*two*three*four

if __name__ == '__main__':
    main()