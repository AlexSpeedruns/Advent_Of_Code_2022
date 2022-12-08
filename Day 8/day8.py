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
    score = 1
    early = False
    if y > 0:
        count = 1
        for i in range(y-1, -1, -1):
            if grid[x][i] < current:
                count += 1
            else:
                score *= count
                early = True
                break
        if not early:
            score *= count-1
    else:
        return 0
    early = False
    if y < 98:
        count = 1
        for i in range(y+1, 99):
            if grid[x][i] < current:
                count += 1
            else:
                score *= count
                early = True
                break
        if not early:
            score *= count-1
    else:
        return 0
    early = False
    if x > 0:
        count = 1
        for i in range(x-1, -1, -1):
            if grid[i][y] < current:
                count += 1
            else:
                score *= count
                early = True
                break
        if not early:
            score *= count-1
    else:
        return 0
    early = False
    if x < 98:
        count = 1
        for i in range(x+1, 99):
            if grid[i][y] < current:
                count += 1
            else:
                score *= count
                early = True
                break
        if not early:
            score *= count-1
    else:
        return 0
    return score

if __name__ == '__main__':
    main()