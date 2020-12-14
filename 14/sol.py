def part1(f):
    data = [line for line in f]
    mem = {}
    mask = "0"
    mask_1 = "0"
    mask_2 = "0"
    for line in data:
        if "mask" in line:
            mask = line[len("mask = "):].strip()
            mask_1 = mask.replace("X", "0")
            mask_2 = mask.replace("X", "1")
        else:
            i = line.index("[") + 1
            j = line.index("]")
            val_index = line.index("=") + 2
            loc = int(line[i:j])
            val = int(line[val_index:])
            new_val = (val | int(mask_1, base=2)) & int(mask_2, base=2)
            mem[loc] = new_val
    return sum(mem.values())

def generateAllBinary(mask):
    x_indices = []
    for i, c in enumerate(mask):
        if c == "X":
            x_indices.append(i)
    return generateAllBinaryStrings(len(mask), list(mask), 0, x_indices)

def generateAllBinaryStrings(n, arr, x, x_indices):
    if x >= len(x_indices):
        yield "".join(arr)
        return
    i = x_indices[x]
    arr[i] = "0"
    yield from generateAllBinaryStrings(n, arr[:], x + 1, x_indices)

    i = x_indices[x]
    arr[i] = "1"
    yield from generateAllBinaryStrings(n, arr[:], x + 1, x_indices)


def part2(f):
    data = [line for line in f]
    mem = {}
    mask = "0"
    mask_1 = "0"
    mask_2 = "0"
    for line in data:
        if "mask" in line:
            mask = line[len("mask = "):].strip()
        else:
            i = line.index("[") + 1
            j = line.index("]")
            val_index = line.index("=") + 2
            loc = int(line[i:j])
            val = int(line[val_index:])

            loc_bin = str(bin(loc))[2:]

            new_mask = list(mask)
            for i in range(-1, -len(loc_bin) - 1, -1):
                if loc_bin[i] == '1' and mask[i] == '0':
                    if i == -1:
                        new_mask = new_mask[:i] + ["1"]
                    else:
                        new_mask = new_mask[:i] + ["1"] + new_mask[i + 1:]

            masks = generateAllBinary(new_mask)
            for m in masks:
                new_loc = int(m, base=2)
                mem[new_loc] = val

    return sum(mem.values())

with open("input") as f:
    print("Day 12 Part 1:", part1(f))
with open("input") as f:
    print("Day 12 Part 2:", part2(f))
