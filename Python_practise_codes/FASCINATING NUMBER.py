num = input("Enter your number :")
pos = 1
n = ""
length = len(n)
while len(n) < 9:
    num1 = int(num)
    result = num1 * pos
    n += str(result)
    pos += 1
    n1 = sorted(n)
print(n)
if n1 == list("123456789"):
    print(True)
else:
    print(False)
