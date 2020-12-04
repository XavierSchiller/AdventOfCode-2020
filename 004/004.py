with open("004.in") as f:
    data = f.read()

passlist = data.split("\n\n")

all_feilds = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

required_feilds = all_feilds[:-1]

# cid as optional

def part1(required_feilds):
    counter = 0
    for passport in passlist:
        passport = passport.replace("\n"," ")
        feilds = [f[0:3] for f in passport.split(" ")]
        if all([rf in feilds for rf in required_feilds]):
            counter+=1

    return counter
print("Part 1:", part1(required_feilds));


hcl_range = [str(x) for x in range(0,10)] + ["a", "b", "c", "d", "e", "f"]

# Fuck this shit lmao
def chk_feild(f):
    if f[0:3] == "byr":
        val = int(f[4:])
        if 1920 <= val <= 2020:
            return True
    
    elif f[0:3] == "iyr":
        val = int(f[4:])
        if 2010 <= val <= 2020:
            return True
    
    elif f[0:3] == "eyr":
        val = int(f[4:])
        if 2020 <= val <= 2030:
            return True
    
    elif f[0:3] == "hgt":
        mes = f[len(f)-2:]
        if mes not in ["in", "cm"]:
            return False
        val = int(f[4:len(f)-2])
        if mes == "in" and  59 <= val <= 76:
            return True
        if mes == "cm" and 150 <= val <= 193:
            return True
    
    elif f[0:3] == "hcl":
        if f[4] != "#" and len(f[5:]) != 6:
            return False
        if all([char in hcl_range for char in f[5:]]):
            return True

    elif f[0:3] == "ecl":
        if f[4:] in ["amb", "blu", "brn", "gry","grn",  "hzl", "oth"]:
            return True
    
    elif f[0:3] == "pid":
        if len(f[4:]) == 9 and all(int(x) in range(0,10) for x in f[4:]):
            return True
    
    else: #cid
        return True
    return False
        


def part2(required_feilds):
    counter = 0
    for passport in passlist:
        passport = passport.replace("\n"," ")
        feilds = passport.split(" ")
        chk = [f[0:3] for f in passport.split(" ")]
        if all([rf in chk for rf in required_feilds]) and all([chk_feild(rf) for rf in feilds]):
            counter+=1
    return counter


print("Part 2:", part2(required_feilds))
