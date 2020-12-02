with open("002.in") as f:
    data = f.readline()
    counter = 0
    while(data != ""):
        left, right = data.rstrip("\n").split(":");
        
        rlen, char = left.split(" ");
        rlens, rlenend = [int(x) for x in rlen.split("-")]

        char = char.lstrip(" ")

        right = right.lstrip(" ")

        val = right.count(char)

        if rlens <= val <= rlenend:
            counter += 1
        
        data = f.readline();

    print(counter)
        
