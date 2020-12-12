
def part1(f):
    x, y = 0, 0
    curr_dir = "E"
    directions = ["N", "E", "S", "W"]
    instructions = [line for line in f]

    for i in instructions:
        offset = int(i[1:])
        direction = i[0]
        if "L" in direction:
            index = directions.index(curr_dir)
            curr_dir = directions[(index - offset//90) % 4]
            continue

        if "R" in direction:
            index = directions.index(curr_dir)
            curr_dir = directions[(index + offset//90) % 4]
            continue

        if "F" in direction:
            direction = curr_dir

        if "N" in direction:
            y += offset
        if "S" in direction:
            y -= offset
        if "E" in direction:
            x += offset
        if "W" in direction:
            x -= offset
    return abs(x) + abs(y)

def part2(f):
    x, y = 0, 0
    way_x, way_y = 10, 1
    cur_dir = "E"
    instructions = [line for line in f]

    for i in instructions:
        offset = int(i[1:])
        direction = i[0]
        if "L" in direction:
            for i in range(offset//90):
                way_x, way_y = -way_y, way_x
            continue

        if "R" in direction:
            for i in range(offset//90):
                way_x, way_y = way_y, -way_x
            continue

        if "F" in direction:
            x += offset*way_x
            y += offset*way_y

        if "N" in direction:
            way_y += offset
        if "S" in direction:
            way_y -= offset
        if "E" in direction:
            way_x += offset
        if "W" in direction:
            way_x -= offset
    return abs(x) + abs(y)


with open("input") as f:
    print("Day 12 Part 1:", part1(f))
with open("input") as f:
    print("Day 12 Part 2:", part2(f))
