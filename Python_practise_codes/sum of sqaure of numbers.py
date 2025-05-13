number = input("Enter the value: ")

while True:
    number = list(map(int, number)) 
    sum = 0

    for i in number:
        square = i ** 2
        sum += square

    if sum < 10:
        break
    else:
        number = str(sum)

print("Final single-digit square sum:", sum)
