
start = int(input("number :"))
end = int(input("Number :"))
for i in range(start, end + 1):
    number = str(i)
    length = len(number)
    total = 0
    for d in number:
        num = int(d)
        cube = num ** length
        total += cube
    if total == i:
        print(total)
    