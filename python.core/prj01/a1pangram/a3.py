i = "abcd"
print(f"i:{i}")
j = reversed(i)
print(f"j: {j}")
k = "".join(j)
print(f"k:{k}")
if i == k:
    print(f"{i} mis palindrome")
else:
    print(f"{i} is not palindrome")
'''
i:abcd
j: <reversed object at 0x0000021B85237E50>
k:dcba
abcd is not palindrome
'''