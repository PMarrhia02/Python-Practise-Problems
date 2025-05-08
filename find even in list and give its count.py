l1 = list(map(int, input("List: ").split()))
new = []
for i in l1:
    if i % 2 == 0:
        new.append(i)
        length  = len(new)
print(new, length)