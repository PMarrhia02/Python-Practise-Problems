"""Find the Largest Number: Given a list of numbers, find the largest one."""

def largest():
    numbers = list(map(int,input("Enter your numbers : ").split()))
    largest_num =numbers[0]
    for i in numbers:
        if i > largest_num:
            largest_num = i
    print(largest_num)
largest()        