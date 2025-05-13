#Check for Prime Number: Write a function to check whether a number is prime or not.
def prime():
    num = int(input("Enter a number: "))
    if num <= 1:
        print("Its not Prime")
    for i in range(2, num):
        if (num % i == 0):
            print("Its not Prime")
            return
     
    print("Its Prime")
    n2 = str(num)
    result = n2[::-1]
    if result == n2:
        print("Its prime Pallindrome")
    else:
        print("Not Prime Pallindrome")
        
prime()