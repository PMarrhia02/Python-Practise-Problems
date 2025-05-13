arr = input("Enter your numbers :")
arr2 = list(map(int,arr.split()))
arr2.sort()
num = []
for i in arr2:
    if i not in num:
        num += [i]
if num == arr2:
    print("Unique")
else:
    print("Not")
            
print(num)