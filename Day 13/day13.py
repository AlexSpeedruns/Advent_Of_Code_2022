from os.path import dirname, join
import json

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        input = file.read()

    sum = 0
    pairs = [pair for pair in input.split("\n\n")]
    packets = [[[2]],[[6]]]
    for i in range(len(pairs)):
        pair_arr = pairs[i].split("\n")
        left = json.loads(pair_arr[0])
        right = json.loads(pair_arr[1])
        packets.append(left)
        packets.append(right)
        if compare(left, right) == -1:
            sum += (i+1)
    print(sum)

    for i in range(1, len(packets)):
        current = packets[i]
        j = i-1
        while j >= 0 and compare(current, packets[j]) == -1:
            packets[j+1] = packets[j]
            j -= 1
        packets[j+1] = current

    for i in range(len(packets)):
        if packets[i] == [[2]]:
            two = i+1
        elif packets[i] == [[6]]:
            six = i+1
    print(two*six)

def compare(left, right):
    if type(left) is int and type(right) is int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif type(left) is int and type(right) is list:
        return compare([left], right)
    elif type(left) is list and type(right) is int:
        return compare(left, [right])
    elif len(left) == 0 and len(right) > 0:
        return -1
    elif len(left) > 0 and len(right) == 0:
        return 1
    elif len(left) == 0 and len(right) == 0:
        return 0
    else:
        value = compare(left[0], right[0])
        if value == 0:
            return compare(left[1:], right[1:])
        else:
            return value

if __name__ == '__main__':
    main()