with open("input") as f:
    arr = []
    for line in f:
        arr.append(int(line))
    arr.sort()
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] < 2020:
            i += 1
        elif arr[i] + arr[j] > 2020:
            j -= 1
        else:
            break
    print("Day 1 Part 1:", arr[i] * arr[j])

with open("input") as f:
    arr = []
    for line in f:
        arr.append(int(line))
    arr.sort()
    stop = False
    for k in range(0, len(arr) - 2):
        i, j = k + 1, len(arr) - 1
        while i < j:
            if arr[k] + arr[i] + arr[j] < 2020:
                i += 1
            elif arr[k] + arr[i] + arr[j] > 2020:
                j -= 1
            else:
                stop = True
                break
        if stop:
            break
    print("Day 1 Part 2:", arr[k] * arr[i] * arr[j])
