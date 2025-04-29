def count():
    string = input("Enter your string : ")
    vowels = "aeiouAEIOU"
    v = ""
    for char in string:
        if char in vowels:
            v = char + v
    print("Thses are the Vowels : ",v, "\nThis is the count for vowels : ",len(v))
count()
