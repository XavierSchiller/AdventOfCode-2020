import sys

data = [int(x) for x in open(sys.argv[1]).read().split()]


def rolling_set(preamble=25):
    sumset = set(data[:preamble])
    yield (sumset, preamble)
    for idx in range(preamble, len(data)):
        sumset.remove(data[idx - preamble])
        sumset.add(data[idx])
        if idx + 1 < len(data):
            yield (sumset, idx + 1)
        else:
            yield (sumset, None)


def sum_find(sumset, sum):
    for val in sumset:
        if (sum - val) in sumset and (sum - val) != val:
            return (val, sum - val)
    return None


def find_first_fault(preamble=25):
    for x, idx in rolling_set(preamble):
        if idx is not None:
            if sum_find(x, data[idx]) is None:
                return (data[idx], idx)


def find_contig():
    fsum, fidx = find_first_fault(25)

    for idx in range(0, fidx - 1):
        ssum = 0
        slist = []
        while ssum < fsum:
            ssum += data[idx]
            slist.append(data[idx])
            idx += 1

        if ssum == fsum:
            return max(slist) + min(slist)


print("Part A: ", find_first_fault()[0])

print("Part B: ", find_contig())
