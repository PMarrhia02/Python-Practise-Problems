"""num = int(input("Number : \n"))


for i in range(11):
    if i<=1:
        continue
    print(num ** i)"""

n = int(input("Number : "))
power = lambda x: n ** x

for i in range(1, 11):
    print(n, f"power {i} = {power(i)}")


