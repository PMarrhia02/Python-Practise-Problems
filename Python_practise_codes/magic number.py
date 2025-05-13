#magic Number
number  = input("Enter your Number :")
while True:
    number = list(map(int,number))
    total = 0
    for i in number:
        n = int(i)
        total += n  
    if total == 1:
        print(total,True)
        break
    elif total < 10:
        print("Not magic")
        break
    else:
        number = str(total)
        number
        
