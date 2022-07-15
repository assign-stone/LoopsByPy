for i in range(0,4):
    for j in range(8, 8-2*i, -1):
        print(" ", end="")
    for k in range(1, 8-2*i):
        print(" *", end="")
    print(" ")
