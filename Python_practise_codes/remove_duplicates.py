#Remove duplicate characters
string = input("String : ")
new = ""
for char in string:
    if char not in new:
        new += char
print(new)
        