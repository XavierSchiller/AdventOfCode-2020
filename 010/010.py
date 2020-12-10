import sys

data = sorted(list(map(int, open(sys.argv[1]).read().split())))


def count_difference():
    three_count = 1
    one_count = 1
    for (x, y) in zip(data, data[1:]):
        if y - x == 1:
            one_count += 1
        elif y - x == 3:
            three_count += 1

    return three_count * one_count


def count_perms():
    indata = list(reversed([0] + data + [max(data) + 3]))

    lookup = {indata[0]: 0, indata[1]: 1}

    for x in indata[2:]:
        # jolts x+1 x+2 x+3 can be reached.
        nodesum = 0
        if x + 1 in lookup:
            nodesum += lookup[x + 1]

        if x + 2 in lookup:
            nodesum += lookup[x + 2]

        if x + 3 in lookup:
            nodesum += lookup[x + 3]

        lookup[x] = nodesum

    return lookup[0]


print("Part A: ", count_difference())
print("Part B: ", count_perms())