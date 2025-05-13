"""def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

numbers = list(map(int,input("Enter your numbers :").split()))
result = sum(*numbers)
print(result)

def sub(*args):
    diff = 0
    for i in args:
        diff -= i
    return diff
numbers = list(map(int,input("Enter your numbers :").split()))
result = sub(*numbers)
print(result)

def mult(*args):
    mult = 1
    for i in args:
        mult *= i
    return mult
numbers = list(map(int,input("Enter your numbers :").split()))
result = mult(*numbers)
print(result)"""

print("Below written operations can be performed :\n 1. Addition \n  2. Subtraction \n 3. Multiplication \n")
Operation_To_Perform = input("Enter operation : ")
if Operation_To_Perform == "1":
    

