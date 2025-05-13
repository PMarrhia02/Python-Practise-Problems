#Take a list of numbers and return a new list with only prime numbers.
number = input("Number :")
num = list(map(int,number.split()))
prime = []
for i in num:
    if i <= 1:
        print("Not prime")
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)
print("prime in list :",prime)