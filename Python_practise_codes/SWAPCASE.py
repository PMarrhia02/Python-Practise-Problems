string = input("enter your string : ")
swapped = ""
for char in string:
    if char.islower():
        swapped += char.upper()
    elif char.isupper():
        swapped += char.lower()
    else:
        swapped += char
print("Swapped : ", swapped)