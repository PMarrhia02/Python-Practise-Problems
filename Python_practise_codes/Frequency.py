#find Frequency
from collections import Counter
string  = input("string : ")
new = Counter(string.split())
print(new)
"""new = ""
for char in string:
    if char not in new:
        new += char
        count = string.count(char)
        print(f"{char} : {count}")"""
        


        
