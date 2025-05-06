#Neon number
number = input("Enter number : ")
n = int(number)
sum = 0
sq = n * n
sq = str(sq)
for i in sq:
    d = int(i)
    sum += d
if sum == n:
    print(True)
else:
    print( False)

    