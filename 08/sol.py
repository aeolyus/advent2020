with open("input") as f:
    instructions = [line for line in f]
    i = 0
    visited_instr = set()
    accumulator = 0
    while True:
        if i in visited_instr:
            break
        visited_instr.add(i)
        instr = instructions[i]
        temp = instr.split()
        op = temp[0]
        offset = int(temp[1])
        if op == "acc":
            accumulator += offset
            i += 1
        elif op == "jmp":
            i += offset
        elif op == "nop":
            i += 1
    print("Day 8 Part 1:", accumulator)

with open("input") as f:
    instructions = [line.strip() for line in f]
    def test(instructions):
        accumulator = 0
        i = 0
        visited_instr = set()
        while i < len(instructions):
            if i in visited_instr:
                return False
            visited_instr.add(i)
            instr = instructions[i]
            temp = instr.split()
            op = temp[0]
            offset = int(temp[1])
            if op == "acc":
                accumulator += offset
                i += 1
            elif op == "jmp":
                i += offset
            elif op == "nop":
                i += 1
        return accumulator

    for i in range(len(instructions)):
        new_instr = instructions[:]
        temp = new_instr[i].split()
        if temp[0] == "jmp":
            new_instr[i] = "nop " + temp[1]
        elif temp[0] == "nop":
            new_instr[i] = "jmp " + temp[1]
        else:
            continue
        res = test(new_instr)
        if res:
            print("Day 8 Part 2:", res)
