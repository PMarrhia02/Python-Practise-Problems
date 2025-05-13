#Swap Two Numbers Without a Temp Variable.

def swap():
    a = int(input("Enter your first number "))
    b = int(input("Enter your second number "))
    print("Before swapping: " ,"a = ", a ,"b = ",b)

    a, b = b, a
    print("After swapping: " ,"a = ", a ,"b = ",b)
swap()