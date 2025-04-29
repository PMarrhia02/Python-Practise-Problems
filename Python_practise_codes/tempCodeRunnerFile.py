num =  int(input("Enter number :"))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(sum,"Its Perfect")
else:
    print("Not Perfect")
        
    
    