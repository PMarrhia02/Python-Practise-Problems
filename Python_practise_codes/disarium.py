number = input("number: ")
original = int(number)
l = len(number)
total = 0
pos = 1

for digit in number:
    num = int(digit)
    total += num ** pos
    pos += 1

if total == original:
    print("True - It is a Disarium Number")
else:
    print("False - It is not a Disarium Number")