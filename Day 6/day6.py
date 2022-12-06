from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        input = file.readline()

    for i in range(4, len(input)):
        group = input[i-4:i]
        if len(set(group)) == 4:
            print(i)
            break

    for i in range(14, len(input)):
        group = input[i-14:i]
        if len(set(group)) == 14:
            print(i)
            break

if __name__ == '__main__':
    main()