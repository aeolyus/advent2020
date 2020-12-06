with open("input") as f:
    result = 0
    chars = set()
    for line in f:
        if len(line) > 1:
            line = line.replace("\n", "")
            chars.update(set(line))
        else:
            result += len(chars)
            chars = set()
    result += len(chars)
    print("Day 6 Part 1:", result)

with open("input") as f:
    data = f.read().split("\n\n")
    result = 0
    for group in data:
        group_data = []
        temp = set()
        for c in group:
            if c == '\n':
                group_data.append(list(temp))
                temp = set()
            else:
                temp.add(c)
        if len(temp) > 0:
            group_data.append(list(temp))
        group_result = list(group_data[0])
        for c in group_data[0]:
            for g in group_data:
                if c not in g and c in group_result:
                    group_result.remove(c)
        result += len(group_result)
    print("Day 6 Part 2:", result)
