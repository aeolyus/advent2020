import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

def check_valid(pair):
    ok = True
    key = pair[0]
    value = pair[1]
    if key == "byr":
        v = int(value)
        ok &= len(value) == 4 and (1920 <= v and v <= 2002)
    if key == "iyr":
        v = int(value)
        ok &= len(value) == 4 and (2010 <= v and v <= 2020)
    if key == "eyr":
        v = int(value)
        ok &= len(value) == 4 and (2020 <= v and v <= 2030)
    if key == "hgt":
        if "cm" in value:
            value = value.replace("cm", "")
            v = int(value)
            ok &= (150 <= v and v <= 193)
        elif "in" in value:
            value = value.replace("in", "")
            v = int(value)
            ok &= (59 <= v and v <= 76)
        else:
            ok = False
    if key == "hcl":
        ok &= len(re.findall("^#[0-9a-f]{6}$", value)) == 1
    if key == "ecl":
        ok &= value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if key == "pid":
        ok &= len(value) == 9 and len(re.findall("^[0-9]*$", value)) == 1
    return ok

with open("input") as f:
    num_valid_passports = 0
    passports = [""]
    i = 0
    for passport in f:
        if passport == "\n":
            i += 1
            passports.append("")
        else:
            passports[i] += passport
            passports[i] = passports[i].replace("\n", " ")

    for passport in passports:
        deets = passport.split(" ")
        more_deets = [i.split(":") for i in deets]
        ok = True
        valid = set()
        cid_present = False
        for pair in more_deets:
            if len(pair) < 2:
                continue
            key = pair[0]
            if key in required:
                valid.add(key)
            if key == "cid":
                cid_present = True

        num_valid = len(valid)
        if ok and (
            num_valid == 8
                or (num_valid == 7 and cid_present == False)
        ):
            num_valid_passports += 1
    print("Day 4 Part 1", num_valid_passports)

with open("input") as f:
    num_valid_passports = 0
    passports = [""]
    i = 0
    for passport in f:
        if passport == "\n":
            i += 1
            passports.append("")
        else:
            passports[i] += passport
            passports[i] = passports[i].replace("\n", " ")

    for passport in passports:
        deets = passport.split(" ")
        more_deets = [i.split(":") for i in deets]
        ok = True
        valid = set()
        cid_present = False
        for pair in more_deets:
            if len(pair) < 2:
                continue
            key = pair[0]
            if key in required:
                valid.add(key)
            if key == "cid":
                cid_present = True
            ok &= check_valid(pair)

        num_valid = len(valid)
        if ok and (
            num_valid == 8
                or (num_valid == 7 and cid_present == False)
        ):
            num_valid_passports += 1
    print("Day 4 Part 2", num_valid_passports)
