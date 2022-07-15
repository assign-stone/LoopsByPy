n = 8
for i in range(2, n):
    for j in range(1, i):
        print("*", end="")
    for k in range(1, 1+i):
        print(" ", end="")
    print(" ")
