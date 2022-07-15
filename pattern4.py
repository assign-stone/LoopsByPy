n = int(input("enter the number: "))
m = 5
for i in range(0, n):
    for j in range(m, 1+i, -1):
        print("*", end="")
    for k in range(1, i):
        print(" ", end="")
    print(" ")
