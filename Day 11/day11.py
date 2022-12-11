from os.path import dirname, join

def main(part):
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        input = file.read()

    items = [[],[],[],[],[],[],[],[]]
    count = [0,0,0,0,0,0,0,0]
    ops = []
    amounts = []
    test_nums = []
    true_monkeys = []
    false_monkeys = []
    monkey_lines = input.split("\n\n")
    for i in range(len(monkey_lines)):
        start_nums = monkey_lines[i].split("\n")[1].strip().split(":")[1].split(",")
        ops.append(monkey_lines[i].split("\n")[2].strip().split()[4])
        amounts.append(monkey_lines[i].split("\n")[2].strip().split()[-1])
        test_nums.append(int(monkey_lines[i].split("\n")[3].strip().split()[-1]))
        true_monkeys.append(int(monkey_lines[i].split("\n")[4].strip().split()[-1]))
        false_monkeys.append(int(monkey_lines[i].split("\n")[5].strip().split()[-1]))
        for num in start_nums:
            items[i].append(int(num))

    if part == 1:
        x = 20
    else:
        x = 10000
        mod = 1
        for num in test_nums:
            mod *= num

    for _ in range(x):
        for i in range(len(monkey_lines)):
            for j in range(len(items[i])):
                count[i] += 1
                worry = items[i][j]
                operation = ops[i]
                amount = amounts[i]
                if amount == "old":
                    amount = worry
                else:
                    amount = int(amount)
                if operation == "*":
                    worry *= amount
                else:
                    worry += amount
                if part == 1:
                    worry = worry // 3
                else:
                    worry = worry % mod
                test_num = test_nums[i]
                true_monkey = true_monkeys[i]
                false_monkey = false_monkeys[i]
                if worry % test_num == 0:
                    items[true_monkey].append(worry)
                else:
                    items[false_monkey].append(worry)
            items[i].clear()
    count.sort()
    print(count[-1] * count[-2])

if __name__ == '__main__':
    main(1)
    main(2)