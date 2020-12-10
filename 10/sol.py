import functools

def part1(f):
    adapters = [int(line) for line in f]
    curr = 0
    highest = max(adapters) + 3
    one_diff = 0
    three_diff = 0
    while curr + 3 < highest:
        temp = [a for a in adapters if a - curr <= 3]
        used = min(temp)
        adapters.remove(used)
        diff = used - curr
        if diff == 1:
            one_diff += 1
        elif diff == 3:
            three_diff += 1
        curr = used
    three_diff += 1
    print("Day 1 Part 2:", one_diff * three_diff)

@functools.lru_cache
def dfs(curr, highest, adapters):
    count = 0
    if curr + 3 >= highest:
        return 1
    temp = [a for a in adapters if 0 < a - curr <= 3]
    for a in temp:
        count += dfs(a, highest, tuple(adapters))
    return count

def part2(f):
    adapters = [int(line) for line in f]
    curr = 0
    highest = max(adapters) + 3
    result = dfs(curr, highest, tuple(adapters))
    print("Day 10 Part 2:", result)

with open("input") as f:
    part1(f)
with open("input") as f:
    part2(f)
