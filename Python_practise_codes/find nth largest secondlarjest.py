number = list(map(int,input("enter your number : ").split()))
n = int(input("enter your number : "))
maxc = number[0]
for i in number:
    if i > maxc:
        maxc = i
print(maxc)
second = number[0]
for i in number:
    if i > second and i < maxc:
        second = i
print(second)

number2 = list(set(number))
for _ in range(n):
    maxval = number2[0]
    n_max = 0
    for i in number2:
        if i > maxval:
            maxval = i
    n_max = maxval
    number2.remove(maxval)
        
print(n_max)
    


