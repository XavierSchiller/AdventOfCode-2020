with open("005.in") as f:
    data = f.read().split("\n")


def find_seat(bpass: str):
    rsta = 0
    rend = 127

    csta = 0
    cend = 7

    for char in bpass:
        if char == "F":
            rend = (rsta + rend)//2
        if char == "B":
            rsta = (rsta + rend)//2 + 1
        if char == "R":
            csta = (csta + cend)//2 + 1
        if char == "L":
            cend = (csta + cend)//2


    return (rend * 8) + cend


#print(find_seat("FBFBBFFRLR"))
#print(find_seat("BFFFBBFRRR"))
#print(find_seat("FFFBBBFRRR"))
#print(find_seat("BBFFBBFRLL"))

def find_highest():
    return max([find_seat(x) for x in data])

print(find_highest())

def find_my_seat():
    seats = sorted([find_seat(x) for x in data])
    low, high = seats[0], seats[-1]

    for lhs, rhs in zip(seats,range(low, high)):
        if lhs != rhs:
            return rhs


print(find_my_seat())

