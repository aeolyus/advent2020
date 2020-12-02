with open("input") as f:
    rules = {}
    passwords = []
    correct = 0
    for i, line in enumerate(f):
        strings = line.split()
        p = strings[2]
        passwords.append(p)
        rule = strings[0].split("-")
        l = strings[1][0]
        rules[(i, p)] = (l, int(rule[0]), int(rule[1]))
    for i in range(len(passwords)):
        p = passwords[i]
        l = rules[(i, p)][0]
        lo = rules[(i, p)][1]
        hi = rules[(i, p)][2]
        if passwords[i].count(l) >= lo and passwords[i].count(l) <= hi:
            correct += 1
    print("Day 2 Part 1:", correct)

with open("input") as f:
    rules = {}
    passwords = []
    correct = 0
    for i, line in enumerate(f):
        strings = line.split()
        p = strings[2]
        passwords.append(p)
        rule = strings[0].split("-")
        l = strings[1][0]
        rules[(i, p)] = (l, int(rule[0]), int(rule[1]))
    for i in range(len(passwords)):
        p = passwords[i]
        l = rules[(i, p)][0]
        lo = rules[(i, p)][1]
        hi = rules[(i, p)][2]
        onlyOne = 0
        if lo - 1 < len(p) and p[lo - 1] == l:
            onlyOne += 1
        if hi - 1 < len(p) and p[hi - 1] == l:
            onlyOne += 1
        if onlyOne == 1:
            correct += 1
    print("Day 2 Part 2:", correct)
