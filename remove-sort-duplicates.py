string = input("Numbers :").split()
l1 = list(map(int,string))
new = []
for num in l1:
    if num not in new:
        new.append(num)
        new.sort()
print(new)