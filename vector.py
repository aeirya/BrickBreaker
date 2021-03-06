from turtle import Vec2D

class Vector:
    def __init__(self, x=(0,0) ,y=None):
        if y == None:
            x,y = x
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def r(self):
        return (self.x, self.y)

    def size(self):
        from math import sqrt
        return sqrt(self.x**2 + self.y**2)

    def angle(self):
        from math import atan2, degrees
        return degrees(atan2(self.y, self.x))

    @staticmethod
    def tuppleInit(r):
        x,y = r
        return Vector(x,y)

    @staticmethod 
    def polarInit(r,t):
        from math import cos,sin,radians
        t = radians(t)
        return Vector(r*cos(t), r*sin(t))

    @staticmethod
    def i(t):
        return Vector.polarInit(1,t)

    def __add__(self, v):
        return __class__(self.x + v.x, self.y + v.y)
    
    def __sub__(self, v):
        return self + v*-1

    def __mul__(self, x):
        return __class__(x* self.x, x* self.y)
    
    def __truediv__(self, x):
        return  self * (1/x)

    def __str__(self):
        return str(self.r())

    def tupple(self):
        return self.x, self.y

    def toVec2D(self):
        return Vec2D(self.x, self.y)
