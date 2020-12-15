def sol(f, get):
    data = [line for line in f]
    data = data[0].strip().split(",")
    data = [int(d) for d in data]
    last_turn = {}

    for i in range(len(data)):
        last_turn[data[i]] = i
        last_spoken = data[i]

    last_turn.pop(data[-1])

    for i in range(len(data), get):
        new_num = 0
        if last_spoken in last_turn:
            new_num = i - last_turn[last_spoken] - 1
        last_turn[last_spoken] = i - 1
        last_spoken = new_num
    return last_spoken

with open("input") as f:
    print("Day 12 Part 1:", sol(f, 2020))
with open("input") as f:
    print("Day 12 Part 1:", sol(f, 30000000))
