# positive negative or 0
def check():
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive Number")
    elif num < 0:
        print("Negative Number")
    else:
        print("It is an Zero")

check()