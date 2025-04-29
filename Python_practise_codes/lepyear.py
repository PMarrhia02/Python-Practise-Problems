def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Its leap year")
    else:
        print("Not a leap year")
leapyear(2000)

start = int(input("Enter starting  year : "))
end = int(input("Enter ending year : "))
for i in range(start, end + 1):
    if(i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i,"Its Leap Year")
    else:
        print(i,"Not Leap Year")
    
