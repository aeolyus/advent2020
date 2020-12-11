def count_adjacent_full(matrix, i, j):
    count = 0
    if j + 1 < len(matrix[i]) and matrix[i][j + 1] == "#":
        count += 1
    if i + 1 < len(matrix) and matrix[i + 1][j] == "#":
        count += 1
    if j - 1 >= 0 and matrix[i][j - 1] == "#":
        count += 1
    if i - 1 >= 0 and matrix[i - 1][j] == "#":
        count += 1

    if j + 1 < len(matrix[i]) and i + 1 < len(matrix) and matrix[i + 1][j + 1] == "#":
        count += 1
    if j + 1 < len(matrix[i]) and i - 1 >= 0 and matrix[i - 1][j + 1] == "#":
        count += 1
    if j - 1 >= 0 and i - 1 >= 0 and matrix[i - 1][j - 1] == "#":
        count += 1
    if j - 1 >= 0 and i + 1 < len(matrix) and matrix[i + 1][j - 1] == "#":
        count += 1
    return count


def check_ok(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def count_first_full(matrix, i, j):
    count = 0
    old_i = i
    old_j = j
    while check_ok(matrix, i, j + 1):
        j += 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    j = old_j
    while check_ok(matrix, i + 1, j):
        i += 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    i = old_i

    while check_ok(matrix, i, j - 1):
        j -= 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    j = old_j

    while check_ok(matrix, i - 1, j):
        i -= 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    i = old_i

    while check_ok(matrix, i + 1, j + 1):
        i += 1
        j += 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    i = old_i
    j = old_j

    while check_ok(matrix, i - 1, j + 1):
        i -= 1
        j += 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    i = old_i
    j = old_j

    while check_ok(matrix, i - 1, j - 1):
        i -= 1
        j -= 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    i = old_i
    j = old_j

    while check_ok(matrix, i + 1, j - 1):
        i += 1
        j -= 1
        if matrix[i][j] == "#":
            count += 1
        if matrix[i][j] != ".":
            break
    i = old_i
    j = old_j
    return count


def process(old_matrix, counter, count_threshold):
    matrix = [row[:] for row in old_matrix]
    changed = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            seat = matrix[i][j]
            if seat == "L":
                count = counter(old_matrix, i, j)
                if count == 0:
                    changed = True
                    matrix[i][j] = "#"
            if seat == "#":
                count = counter(old_matrix, i, j)
                if count >= count_threshold:
                    changed = True
                    matrix[i][j] = "L"
    return matrix, changed


def parse(matrix):
    for i in range(len(matrix)):
        row = matrix[i].strip()
        matrix[i] = list(row)


def part1(f):
    matrix = [line for line in f]
    parse(matrix)
    changed = True
    while changed:
        matrix, changed = process(matrix, count_adjacent_full, 4)

    full_seats = 0
    for row in matrix:
        full_seats += row.count("#")
    print("Day 11 Part 1:", full_seats)


def part2(f):
    matrix = [line for line in f]
    parse(matrix)
    changed = True
    while changed:
        matrix, changed = process(matrix, count_first_full, 5)

    full_seats = 0
    for row in matrix:
        full_seats += row.count("#")
    print("Day 11 Part 2:", full_seats)


with open("input") as f:
    part1(f)
with open("input") as f:
    part2(f)
