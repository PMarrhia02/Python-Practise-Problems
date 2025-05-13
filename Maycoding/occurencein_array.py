array = input("Array :")
arr = list(map(int, array.split(' '))) 
new = []
max_val = 0
for i in arr:
    if i not in new:
        new.append(i)
        count= arr.count(i)
        if count > max_val:
            max_val = count
            value = i
print("Total times an element is showing :",max_val ,"and Element is :",value )
        