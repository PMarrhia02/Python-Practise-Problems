string = input("String : ")
new = ""
for char in range(len(string)):
    if char % 2 == 0:
        new += string[char].upper()
    else:
        new += string[char].lower()
print(new)