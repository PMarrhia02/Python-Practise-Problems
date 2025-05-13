#Remove spaces from a string
string = input("String : ")
newS = ""
for char in string:
    if char != " ":
        newS += char
print(newS)
