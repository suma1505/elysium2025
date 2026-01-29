fp = open('drinks.txt', 'w')
fp.write('soft drink categories: orange, apple and mango')
fp.close()
print('\n overwrite a file')

fp = open('drink.txt','r')
s = fp.read()
fp.close()

print('\n File content')
print(s)
'''
overwrite a file

 File content
soft drink categories: orange, apple and mango
'''
