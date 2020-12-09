def check(arr, a, b, num):
    for i in range(a, b):
        for j in range(a, b):
            num1 = arr[i]
            num2 = arr[j]
            if (
                num1 != num2
                and num1 + num2 == num
            ):
                return True
    return False

def find_continugous(arr, num):
    i = 0
    j = 1
    while sum(arr[i:j]) != num:
        temp = sum(arr[i:j])
        if temp < num:
            j += 1
        elif temp > num:
            i += 1
            j = i + 1
        else:
            break
    sol_arr = arr[i:j]
    return min(sol_arr) + max(sol_arr)


with open("input") as f:
    instructions = [int(line) for line in f]
    a = 0
    b = 25
    invalid = None
    for target in instructions[25:]:
        if not check(instructions, a, b, target):
            invalid = target
            print("Day 9 Part 1:", invalid)
            break
        else:
            a += 1
            b += 1
    print("Day 9 Part 2:", find_continugous(instructions, invalid))
