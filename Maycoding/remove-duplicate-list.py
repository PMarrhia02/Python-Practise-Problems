#Remove duplicates from a list.
n = input("List :")
l1 = list(map(int, n.split(' ')))
new = []
for i in l1:
    if i not in new:
        new.append(i)
print(new)