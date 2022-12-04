from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    count_one = 0
    count_two = 0

    for line in lines:
        line_arr = line.split(",")
        first = line_arr[0].split("-")
        second = line_arr[1].split("-")
        first_low = int(first[0].strip())
        first_high = int(first[1].strip())
        second_low = int(second[0].strip())
        second_high = int(second[1].strip())

        if(second_low >= first_low and second_high <= first_high) or (first_low >= second_low and first_high <= second_high):
            count_one += 1
        if first_high >= second_low and first_low <= second_high:
            count_two += 1

    print(count_one)
    print(count_two)

if __name__ == '__main__':
    main()