i = 5
def show():
    i = 1000
    print(f"show:i = {i}")
    return
print(f"main-start:i = {i}")
show()
print(f"main-end:i = {i}")
'''
main-start:i = 5
show:i = 1000
main-end:i = 5
'''