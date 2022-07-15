for i in range(1, 4):
    for j in range(1, 1+i):
        print("*", end="")
    for k in range(1, i):
        print(" ", end="")
    print(" ")
for l in range(0, 2):
    for m in range(0, 2-l):
        print("*", end="")
    for n in range(1, 2+l):
        print(" ", end="")
    print(" ")
