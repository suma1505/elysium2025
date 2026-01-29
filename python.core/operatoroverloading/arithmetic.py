class OPO:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        return
    def __del__(self):
        del self.x, self.y
        return
    def __add__(self, other):
        obj T = OPO()
        obj T.x = self.x + other.x
        obj T.y = self.y + other.y
        return obj T
     def __sub__(self, other):
        obj T = OPO()
        obj T.x = self.x - other.x
        obj T.y = self.y - other.y
        return obj T
     def __mul__(self, other):
        obj T = OPO()
        obj T.x = self.x * other.x
        obj T.y = self.y * other.y
        return obj T
     def __truediv__(self, other):
        obj T = OPO()
        obj T.x = self.x / other.x
        obj T.y = self.y / other.y
        return obj T
     def __mod__(self, other):
        obj T = OPO()
        obj T.x = self.x % other.x
        obj T.y = self.y % other.y
        return obj T
     def __pow__(self, other):
        obj T = OPO()
        obj T.x = self.x ** other.x
        obj T.y = self.y ** other.y
        return obj T
    def __str__(self):
        return f"x:{self.x}\n y:{self.y}
obj A = OPO(23,16)
obj B = OPO(5,4)

obj C = OPO(obj A + obj B)
print(obj C)

obj C = OPO(obj A - obj B)
print(obj C)

obj C = OPO(obj A * obj B)
print(obj C)

obj C = OPO(obj A / obj B)
print(obj C)

obj C = OPO(obj A % obj B)
print(obj C)

obj C = OPO(2,3) ** OPO(4,5)
print(obj C)
    
         
        
    
