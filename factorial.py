# WAP to take an integer from user and calculate its factorial.
f = int(input("write any integer: "))
for i in range(1, f):
    f = f * i
print("Factorial = ", end="")
print(f)
