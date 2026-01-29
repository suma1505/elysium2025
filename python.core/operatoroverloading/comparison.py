class OPO:
    def __init__(self, x):
        self.x = x
        return
    def __del__(self):
        del self.x
        return
    def __str__(self):
        return f"{self.x}"
    def __lt__(self, other):
        return self.x < other.x
    def __gt__(self, other):
        return self.x > other.x
    def __eq__(self, other):
        return self.x == other.x
    def __nq__(self, other):
       return self.x != other.x
    def __le__(self, other):
        return self.x <= other.x
    def __ge__(self, other):
         return self.x >= other.x
obj1 = OPO(7)
obj2 = OPO(4)
obj3 = OPO(7)
print(obj1)
print(obj2)
print(obj3)
print(obj1 == obj2)
print(obj1 == obj3)
print(obj2 == obj3)

print(obj1 != obj2)
print(obj1 != obj3)
print(obj2 != obj3)

print(obj1 < obj2)
print(obj1 < obj3)
print(obj2 < obj3)

print(obj1 > obj2)
print(obj1 > obj3)
print(obj2 > obj3)

print(obj1 <= obj2)
print(obj1 <= obj3)
print(obj2 <= obj3)

print(obj1 >= obj2)
print(obj1 >= obj3)
print(obj2 >= obj3)

'''
7
4
7
False
True
False
True
False
True
False
False
True
True
False
False
False
True
True
True
True
False
'''
