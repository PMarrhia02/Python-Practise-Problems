num = input("Enter your number : ")
total = 0

for i in num:
    d = int(i)
    total += d ** 3 

total = str(total)  

if total.endswith(num):
    print("Trimorphic number")
else:
    print("Not Trimorphic")
    
print("Cube sum:", total)
