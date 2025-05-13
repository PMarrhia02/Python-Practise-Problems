def fact():
    num = int(input("Enter Your Number : "))
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print(fact)
fact()

"""from math import factorial
num = int(input("Enter Your Number : "))
num2 = factorial(num)
print("Factorial of",num,"is",num2)"""

