import re
def isVowel(x):
    if re.match(r'[AEIOUaeiou]', x):
        return "vowel"
    else:
        return "consonant"
print(isVowel('E'))
print(isVowel('d'))
'''
vowel
consonant
'''