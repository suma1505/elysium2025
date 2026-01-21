def isPalindrome(s):
    return True if s == "".join(reversed(s)) else False
x = "abcd"
if isPalindrome(x):
    print(f"{x} is palindrome")
else:
    print(f"{x} is not palindrome")
x = "abba"
if isPalindrome(x):
    print(f"{x} is palindrome")
else:
    print(f"{x} is not palindrome")
'''
abcd is not palindrome
abba is palindrome
'''