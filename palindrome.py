s = input("Enter your palindrome :")
reserve = s[::-1]
if reserve == s :
    print("its valid palindrome")
else :
    print("its not a palindrome")