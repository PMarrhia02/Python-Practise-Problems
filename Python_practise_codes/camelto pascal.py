camel_string = input("Enter your string : ")
string = camel_string.split("_")
s = " "
for word in string:
    if word[0].islower():
        s += word[0].capitalize() + word[1:]
    else:
        s += word
print(s.strip())