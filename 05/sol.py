import math

with open("input") as f:
    seat_ids = []
    for line in f:
        lo = 0
        hi = 127
        r = 7
        l = 0
        for i in range(0, 7):
            instr = line[i]
            if instr == "B":
                delta = math.floor((hi - lo)/2)
                lo = hi - delta
            if instr == "F":
                delta = math.ceil((hi - lo)/2)
                hi = hi - delta
        for i in range(7, 10):
            instr = line[i]
            if instr == "R":
                delta = math.floor((r - l)/2)
                l = r - delta
            if instr == "L":
                delta = math.ceil((r - l)/2)
                r = r - delta
        row = lo
        col = l
        seat = row * 8 + col
        seat_ids.append(seat)
    print("Day 5 Part 1:", max(seat_ids))

import math

with open("input") as f:
    seat_ids = []
    for line in f:
        lo = 0
        hi = 127
        r = 7
        l = 0
        for i in range(0, 7):
            instr = line[i]
            if instr == "B":
                delta = math.floor((hi - lo)/2)
                lo = hi - delta
            if instr == "F":
                delta = math.ceil((hi - lo)/2)
                hi = hi - delta
        for i in range(7, 10):
            instr = line[i]
            if instr == "R":
                delta = math.floor((r - l)/2)
                l = r - delta
            if instr == "L":
                delta = math.ceil((r - l)/2)
                r = r - delta
        row = lo
        col = l
        seat = row * 8 + col
        seat_ids.append(seat)

    seat_ids.sort()
    look_at = None
    last = seat_ids[0]
    for s in seat_ids:
        if s - last > 1:
            look_at = last + 1
        last = s
    print("Day 5 Part 2:", look_at)
