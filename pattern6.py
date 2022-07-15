for i in range(97, 101):
    for j in range(97, 1+i):
        print(chr(j), end="")
    for k in range(101, 1+i, -1):
        print(" ", end="")
    print(" ")
