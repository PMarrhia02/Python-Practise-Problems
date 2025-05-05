string = input("String: ").split()
l1 = list(map(int,string))
largest = l1[0]
for i in l1:
    if largest < i:
        largest = i
nmax = largest
l1.remove(largest)

nmax = l1[0]
for j in l1:
    if nmax < j:
        nmax = j
print(nmax)