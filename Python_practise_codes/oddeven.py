number = int(input("Enter your number: "))
if number <= 0:
    print("Not even Nor odd")
elif number > 0 and number % 2 == 0:
    print("Number is Even")
else:
    print("The number is odd.")