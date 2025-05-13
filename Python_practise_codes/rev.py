def rev():
    String = input("Enter Your String : ")
    rev = ""
    for char in String:
        rev = char + rev
    print(rev)
rev()

