mylist = list(map(int, input("Enter numbers : ").split()))
n= int(input("Number : "))
result = list(filter(lambda x:(x % n == 0), mylist))
print(result)