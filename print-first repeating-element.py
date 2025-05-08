l1 = list(map(int, input("List: ").split()))
new = []
for i in l1:
    if i not in new:
        new.append(i)
    else:
        print(i)
        break
    