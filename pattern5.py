for i in range(1, 5):
    for j in range(1, 1+i):
        print(j, end="")
    for k in range(5, i, -1):
        print(" ", end="")
    print(" ")
