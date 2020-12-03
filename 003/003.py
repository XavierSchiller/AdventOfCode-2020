data = ""
with open("003.in") as f:
    data = f.read()

data = data.split("\n")

rotlen = len(data[0])

def treecount(xskip, yskip):
    xpos = 0
    counter = 0
    for row in data[::yskip]:
        if row[xpos] == "#":
            counter+=1

        xpos = (xpos + xskip) % rotlen

    return counter


print("Solution 1:", treecount(3,1))

print("Solution 2:", treecount(1,1)*treecount(3,1)*treecount(5,1)*treecount(7,1)*treecount(1,2))


