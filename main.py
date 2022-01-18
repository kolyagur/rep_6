from abc import ABC, abstractmethod
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1 or Point()
        self.p2 = p2 or Point()     
   
    def length(self):
        return round(sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y -  self.p1.y) ** 2),2)

class Shape(ABC):
    @property
    @abstractmethod 
    def area(self):
        pass
    
    @property
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape, Line):
    @property  
    def area(self):
        return round(self.length()**2,2)

    @property
    def perimeter(self):
        return round(4*self.length(),2)

class Rect(Shape):
    def __init__(self, r1, r2):
        self.r1 = r1 or Line() 
        self.r2 = r2 or Line()

    @property
    def area(self):
        return round(self.r1.length()*self.r2.length(),2)

    @property
    def perimeter(self):
        return round((self.r1.length()+self.r2.length())*2,2)

class Cube(Square): 
    def volume(self):
       return round(self.length()**3,2)