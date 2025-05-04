string = input("String: ")
new = ""
for char in string:
    if char not in new:
        new += char
        count = string.count(char)
        print(char, count)