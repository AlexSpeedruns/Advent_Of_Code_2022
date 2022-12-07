from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    system = []
    size_dict = {}
    for line in lines:
        line_arr = line.strip().split(" ")
        if line_arr[1] == "ls" or line_arr[0] == "dir":
            continue
        elif line_arr[1] == "cd" and line_arr[2] == "..":
            system.pop()
        elif line_arr[1] == "cd":
            system.append(line_arr[2])
        else:
            for i in range(1, len(system)+1):
                key = "/"
                for j in range(1, i):
                    key += system[j]
                if size_dict.get(key):
                    size_dict[key] += int(line_arr[0])
                else:
                    size_dict[key] = int(line_arr[0])

    sum = 0
    for value in size_dict.values():
        if value <= 100000:
            sum += value

    print(sum)

    remainder = size_dict["/"] - 40000000
    min = 99999999
    for value in size_dict.values():
        if value >= remainder and value < min:
            min = value
    print(min)


if __name__ == '__main__':
    main()