from main import *

a=Point(3,9)
b=Point(9,5)
c=Point(5,39)
d=Point(9,10)
print(f'Точка A: {a.x},{a.y}, Точка B: {b.x},{b.y}')
print(f'Точка C: {c.x},{c.y}, Точка D: {c.x},{c.y}')
#

#
ac=Line(a,c)
ab=Line(a, b)
print(ac.length()) 
print(ab.length()) 
#
Sq=Square(a,b)
print(f'\nПериметр квадрата:{Sq.perimeter} \nПлощадь квадрата:{Sq.area}')
#
Rt=Rect(ab,ac)
print(f'Периметр прямоугольника:{Rt.perimeter} \nПлощадь прямоугольника:{Rt.area}')
#
Cb=Cube(a,b)             
print(f'Объем куба:{Cb.volume()}')