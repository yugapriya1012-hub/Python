def palindrome(s1):
    a=''
    for i in s1:
        a=i+a
    if a==s1:
        print("Palindrome")
    else:
        print("Not a palindrome")
palindrome("mom")


