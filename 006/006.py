# Group is sep by blank lines
# no of lines in group = no of people

import sys 

groups = [x.replace("\n"," ") for x in open(sys.argv[1]).read().split("\n\n")]

def find_anyone(group):
    # Process Each Group
    group = set(group.replace(" ", ""))

    return len(group)


def find_everyone(group):
    sets = [set(x) for x in group.split(" ")]

    intsec = set.intersection(*sets)

    return len(intsec)

print("Part 1:", sum([find_anyone(x) for x in groups]))


print("Part 2:", sum([find_everyone(x) for x in groups]))
