from os.path import dirname, join
from copy import deepcopy

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    move_dict = {
        "U": (0, 1),
        "L": (-1, 0),
        "D": (0, -1),
        "R": (1, 0)
    }

    head = [(0,0)]
    for line in lines:
        line_arr = line.strip().split()
        dir = move_dict[line_arr[0]]
        amount = int(line_arr[1])
        for _ in range(amount):
            head.append((head[-1][0] + dir[0], head[-1][1] + dir[1]))

    tail = calculate_tail(head)
    print(len(set(tail)))

    for _ in range(9):
        tail = calculate_tail(head)
        head = deepcopy(tail)
    print(len(set(tail)))

def calculate_tail(head):
    tail = [(0,0)]
    current_tail = (0,0)
    for pos in head:
        x_dist = abs(pos[0]-current_tail[0])
        y_dist = abs(pos[1]-current_tail[1])
        if x_dist > 1 or y_dist > 1:
            x_change = 0
            y_change = 0
            if pos[0]-current_tail[0] > 0:
                x_change = 1
            elif pos[0]-current_tail[0] < 0:
                x_change = -1
            if pos[1]-current_tail[1] > 0:
                y_change = 1
            elif pos[1]-current_tail[1] < 0:
                y_change = -1
            current_tail = (current_tail[0]+x_change,current_tail[1]+y_change)
        tail.append(current_tail)
    return tail

if __name__ == '__main__':
    main()