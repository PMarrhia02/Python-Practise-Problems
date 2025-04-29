# start = int(input("Enter your number : "))
# end = int(input("Enter your number :"))
# for i in range(start, end + 1):
#     if i <= 1:
#         continue
#     for j in range(2, i):
#         if i % j == 0:
#             print(i,"Its not Prime")
#             break
            
#     else: 
#         print(i, "Its Prime")


# Input string
text = "hi my name is prikshit"
words = text.split()
rs=" "
for word in words:
    first=word[0].upper()
    last=word[-1].upper()
    word=word.replace(word[0],first)
    word=word.replace(word[-1],last)
    rs+=word+" "


print(rs)
