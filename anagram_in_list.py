#Group anagrams from a list of strings
string = input("Enter your Words: ").split(' ')
string.sort()
string.lower()
l1 = {}
for char in string:
    words = list(char)
    words.sort()
    sort = ''.join(words)
    
    if sort not in l1:
        l1[sort] = []
    l1[sort].append(char)

print(l1)