# WAP to take an integer from user and print its table like 2x1=2, 2x2=4…so on

num = int(input("Enter number: "))
for i in range(1, 11):
    a = num * i
    print(str(num)+" x "+str(i)+" = "+str(a))
