number = input("Enter your number: ")
original = int(number)
total = 0
length = len(number)
for i in number:
    num = int(i)
    cube = num ** length
    total += cube
print(total)
if original == total:
    print("Yes The cube is equal to original number. ")
else:
    print("No it is not equal to original number.")