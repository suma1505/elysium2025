import operator as op
def isVowel(x):
    if op.countOf("AEIOUaeiou", x) > 0:
        return "vowel"
    else:
        return "consonant"
print(isVowel('w'))
print(isVowel('a'))
'''
consonant
vowel
'''