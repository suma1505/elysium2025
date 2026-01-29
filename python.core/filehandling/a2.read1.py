fp = open('hot.txt', 'r')
s =fp.read()
fp.close()

print('\n File content \n', s, sep="")
'''
FileNotFoundError: [Errno 2] No such file or directory: 'hot.txt'
'''
