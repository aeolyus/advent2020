def part1(f):
    data = [line for line in f]
    i = 0
    mem = {}
    while data[i] != "\n":
        line = data[i].split(":")
        word = line[0]
        ranges = []
        for r in line[1].split():
            if "or" in r:
                continue
            range_list = r.split("-")
            ranges.append([int(a) for a in range_list])
        i += 1
        mem[word] = ranges

    i += 2
    my_ticket = data[i]
    i += 3

    error_rate = 0
    while i < len(data):
        ticket = data[i]
        ticket_vals = ticket.split(",")
        for str_val in ticket_vals:
            val = int(str_val)
            ok = False
            for range_list in mem.values():
                for smol, big in range_list:
                    if smol <= val <= big:
                        ok = True
            if not ok:
                error_rate += val
        i += 1

    return error_rate

def part2(f):
    data = [line for line in f]
    i = 0
    mem = {}
    while data[i] != "\n":
        line = data[i].split(":")
        word = line[0]
        ranges = []
        for r in line[1].split():
            if "or" in r:
                continue
            range_list = r.split("-")
            ranges.append([int(a) for a in range_list])
        i += 1
        mem[word] = ranges

    i += 2
    my_ticket = data[i]
    i += 3

    error_rate = 0
    ok_tickets = []
    while i < len(data):
        ticket = data[i]
        ticket_vals = [int(t) for t in ticket.strip().split(",")]
        ticket_ok = False
        for val in ticket_vals:
            ok = False
            for range_list in mem.values():
                for smol, big in range_list:
                    if smol <= val <= big:
                        ok = True
                        ticket_ok = True
            if not ok:
                error_rate += val
        i += 1
        if ticket_ok:
            ok_tickets.append(ticket_vals)

    loc = {}
    for i in range(len(mem)):
        for key in mem:
            ok_col = True

            for ticket in ok_tickets:
                ok_ticket = False
                for pair in mem[key]:
                    smol, big = pair[0], pair[1]
                    if (smol <= ticket[i] <= big):
                        ok_ticket = True


                ok_col &= ok_ticket
            if ok_col:
                if key in loc:
                    loc[key] += [i]
                else:
                    loc[key] = [i]
    print(loc)

with open("input") as f:
    print("Day 12 Part 1:", part1(f))
