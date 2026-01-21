fp = open("testa.dat", "rb")
bd = fp.read()
print('\n\ndisplay binary file data, in unreadable format')
print(bd)
print('\n\ndisplay binary file data, in unreadable format')
print(bd.decode('ascii'))
fp.close()
'''


display binary file data, in unreadable format
b'abcdefg\nhijklmn\nopqrstu\nvwxyz\n'


display binary file data, in unreadable format
abcdefg
hijklmn
opqrstu
vwxyz
'''