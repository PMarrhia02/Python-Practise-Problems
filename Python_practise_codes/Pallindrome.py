def pallindrome():
    String = input("Enter a String : ")
    String = String.lower()
    rev = ""
    for i in String:
        rev = i + rev
    if rev == String:
        print("The string is a palindrome")
    else:
        print("The String Is Not Palindrome")
pallindrome()