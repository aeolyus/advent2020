with open("input") as f:
    bag_map = dict()
    for line in f:
        line = line.replace(".", "")
        line = line.replace("\n", "")
        line_arr = line.split(",")
        beginning = line_arr[0].split("contain")
        line_arr.pop(0)
        for j in beginning[::-1]:
            line_arr.insert(0, j)
        line_arr = [s.strip() for s in line_arr]
        line_arr = [s + 's' if s[-1] != 's' else s for s in line_arr]

        outer = line_arr[0]

        sub_result = dict()
        for inner in line_arr[1:]:
            if "no other bags" in inner:
                continue
            else:
                count = int(inner[0])
                inner_type = inner[2:]
                sub_result[inner_type] = count

        bag_map[outer] = sub_result

    res = set()
    stack = ["shiny gold bags"]
    while len(stack) > 0:
        bag = stack.pop(0)
        for o, i in bag_map.items():
            if bag in i:
                stack.append(o)
                res.add(o)
    print("Day 7 Part 1:", len(res))

    def dfs(result, bag):
        for out_bag, count in bag_map[bag].items():
            result += count + count * dfs(0, out_bag)
        return result
    result = dfs(0, "shiny gold bags")
    print("Day 7 Part 2:", result)
