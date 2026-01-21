def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < len(s):
        lr = s[i: i + 1]
        rl = s[j: j + 1]
        if lr != rl:
            return False
        i += 1
        j -= 1
    return True
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