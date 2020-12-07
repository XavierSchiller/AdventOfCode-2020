import sys
from pprint import pprint
data = open(sys.argv[1]).read().split("\n")

conrev = {}
contrev = {}
def proc_contains(string: str):
    string = [x.replace("bags", "").replace("bag", "").strip(". ") for x in contains.split(",")]

    if string[0].startswith("no"):
        return [(0, None)]
    
    proced = []

    for x in string:
        val, color = x.split(" ", 1)
        val = int(val)
        proced.append((val, color))

    return proced

for row in data:
    container, contains = row.split(" contain ")
    contains = proc_contains(contains)
    container = container.replace(" bags", "")
    
    for (val, bag) in contains:
        if bag in conrev:
            conrev[bag].append((container, val))
        else:
            conrev[bag] = [(container,val)]

    contrev[container] = contains

def trace_back(s):
    stk = [s]
    bags = set()
    while stk:
       val = stk.pop()
       if val in conrev:
           for (x,_) in conrev[val]:
               bags.add(x)
               stk.append(x)

    return len(bags)

def trace_forward(s):
    stk = [(1, s)]
    sum = 0
    while stk:
        bsum, cbag = stk.pop()
        sum+= bsum

        if cbag in contrev:
            stk.extend([(val*bsum, bag) for (val, bag) in contrev[cbag]])
        
    return sum - 1 # Because it has the one additional bag from the main bag


print("Part 1: ", trace_back("shiny gold"))

print("Part 2: ", trace_forward("shiny gold"))
