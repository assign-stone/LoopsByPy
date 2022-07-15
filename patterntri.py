for i in range(0, 4):
    for j in range(1, 7-2*i):
        print(" ", end="")
    for k in range(7, 6-i*2, -1):
        print(" $", end="")
    print(" ")
