from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().split("\n\n")

    elves = []
    for elf in lines:
        elf_list = [int(i) for i in elf.split("\n")]
        elves.append(sum(elf_list))

    elves.sort()
    print(elves[-1])
    print(elves[-1]+elves[-2]+elves[-3])

if __name__ == '__main__':
    main()