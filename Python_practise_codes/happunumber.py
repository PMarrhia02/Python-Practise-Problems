number = input("Enter the value: ")

while True:
    number = list(map(int, number))
    total = 0

    for i in number:
        total += i ** 2

    if total == 1:
        print("Happy Number")
        break
    elif total == 4:
        print("Not a Happy Number")
        break
    else:
        number = str(total)
print("Final single-digit square sum:", total)
