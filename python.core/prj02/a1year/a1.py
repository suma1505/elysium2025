def uIsleapyear(year):
    if (year % 100 != 0 or year % 400 == 0 and year % 4 == 0):
        return True
    else:
        return False
try:
    y = int(input("Enter year value:"))
    if uIsleapyear(y):
        print(f"{y} is leap year")
    else:
        print(f"{y} is not leap year")
except Exception as e:
    print(f"err:{e}")
'''
Enter year value:2000
2000 is leap year

Enter year value:3000
3000 is not leap year

Enter year value:4000
4000 is leap year
'''