string = input("Enter the string : ")
punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
new = ""
for char in string:
    if char not in punctuations:
        new += char
print(new)