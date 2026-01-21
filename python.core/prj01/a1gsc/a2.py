i = 5
def show():
    j = 1000
    print(f"show:i = {i}")
    print(f"show:j = {j}")
    return
print(f"main-start:i = {i}")
show()
print(f"main-end:i = {i}")
print(f"main-end:j = {j}")
'''
main-start:i = 5
show:i = 5
show:j = 1000
main-end:i = 5
NameError: name 'j' is not defined
'''