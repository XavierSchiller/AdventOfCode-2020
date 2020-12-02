with open("002.in") as f:
    data = f.readline()
    counter = 0
    while(data != ""):
        left, right = data.rstrip("\n").split(":");
        
        rlen, char = left.split(" ");
        rlens, rlenend = [int(x)-1 for x in rlen.split("-")]

        char = char.lstrip(" ")

        right = right.lstrip(" ")

        if (right[rlens] == char and right[rlenend] != char) or (right[rlens] != char and right[rlenend] == char):
            counter+=1

        data = f.readline()

    print(counter)
        
