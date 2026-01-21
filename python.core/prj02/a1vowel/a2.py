def isVowel(x):
    swicher ={
        'A': 'Vowel',
        'E': 'Vowel',
        'I': 'Vowel',
        'O': 'Vowel',
        'U': 'Vowel',
        'a': 'Vowel',
        'e': 'Vowel',
        'i': 'Vowel',
        'o': 'Vowel',
        'u': 'Vowel',
    }
    return swicher.get(x, 'consonant')
print(isVowel('g'))
print(isVowel('i'))
'''
consonant
Vowel
'''