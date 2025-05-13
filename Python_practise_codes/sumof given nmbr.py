def sum():
    num = input("Enter Your Number : ")
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    print(sum)
sum()
