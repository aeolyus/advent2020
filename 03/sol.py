def find(right, down, f):
    count = 0
    i = 0
    for j in range(down, len(f), down):
        if j >= len(f):
            break
        line = f[j]
        i += right
        i = i % (len(f[0]) - 1)
        string = list(line)
        if string[i] == '#':
            count += 1
    return count

with open("input") as f:
    ans = find(3, 1, f.readlines())
    print("Day 3 Part 1:", ans)

with open("input") as f:
    slope = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    ans = 1
    for a, b in slope:
        ans *= find(a, b, f.readlines())
        f.seek(0)
    print("Day 3 Part 2:", ans)

