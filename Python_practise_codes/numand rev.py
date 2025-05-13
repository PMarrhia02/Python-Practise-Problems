#check num and its rev is prime or not
num = int(input("Enter your number:"))
rev = int(str(num)[::-1]) 
if num <= 1 and rev <= 1:
    print("Not Prime")
for i in range(2, num):
    if (num % i == 0):
        print("Not Prime")
        break
else:
    print("Prime")
if rev <= 1:
    print("not prime")
for i in range(2, rev):
    if rev % i == 0 :
        print("Its not Prime")
        break
else:
    print("Its Prime")
    

    
    
