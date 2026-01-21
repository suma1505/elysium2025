def isPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < len(s):
        lr = s[i: i + 1]
        rl = s[j: j + 1]
        print(i, ":", lr, "=", j, ":", rl)
        i += 1
        j -= 1
x = "abcd"
isPalindrome(x)
'''
0 : a = 3 : d
1 : b = 2 : c
2 : c = 1 : b
3 : d = 0 : a
'''