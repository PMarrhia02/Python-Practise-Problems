numbers = list(map(int,input("List : ").split()))
target = 9
pair = []
for i in range(len(numbers)):
    for j in range(i + 1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i] , numbers[j])
