def part1(f):
    data = [line for line in f]
    time = int(data[0])
    buses = data[1].strip().split(",")
    buses = [int(b) for b in buses if b != "x"]
    new_depart = []
    for b in buses:
        d = b*(time//b)
        if d - time < 0:
            d = b*(time//b + 1)
        new_depart.append(d - time)
    index = new_depart.index(min(new_depart))
    return buses[index] * new_depart[index]

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def part2(f):
    data = [line for line in f][1]
    buses = data.strip().split(",")
    buses = list(enumerate(buses))
    buses = [(-b[0], int(b[1])) for b in buses if b[1] != "x"]
    temp = 0
    N = 1
    for _, i in buses:
        N *= i
    for b, n in buses:
        N_i = N//n
        temp += b * N_i * mod_inverse(N_i, n)
    return temp % N

with open("input") as f:
    print("Day 12 Part 1:", part1(f))
with open("input") as f:
    print("Day 12 Part 2:", part2(f))
