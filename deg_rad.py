from fractions import Fraction
import math
PI = math.pi

def deg_to_rad():
    Rad = Fraction(deg/180)
    print(Rad, "π radians")
    
def rad_to_deg():
    print((rad*180/PI), "degrees")

print("Press 'a' to degree to radian convertion or press 'b' to degree to radian convertion")
x = input("Give your input first: ")

if x == 'a':
    d = input("Give your angle in degrees: ")
    if '+' in d:
        y = d.index('+')
        u = float(d[:y])
        v = float(d[y + 1:])
        deg = u + v
    elif '-' in d:
        y = d.index('-')
        u = float(d[:y])
        v = float(d[y + 1:])
        deg = u - v
    elif '*' in d:
        y = x.index('*')
        u = float(d[:y])
        v = float(d[y + 1:])
        deg = u * v
    elif '/' in d:
        y = x.index('/')
        u = float(d[:y])
        v = float(d[y + 1:])
        deg = u / v
    else:
        deg = float(d)
    deg_to_rad()
elif x == 'b':
    print("Press 'PI' to input π")
    r = input("Give your angle in radian: ")
    if 'PI' in r:
        if '+' in r:
            y = r.index('+')
            v = float(r[y + 1:])
            rad = PI + v
        elif '-' in r:
            y = r.index('-')
            v = float(r[y + 1:])
            rad = PI - v
        elif '*' in r:
            y = r.index('*')
            v = float(r[y + 1:])
            rad = PI * v
        elif '/' in r:
            y = r.index('/')
            v = float(r[y + 1:])
            rad = PI / v
        else:
            rad = PI
    else:
        if '+' in r:
            y = r.index('+')
            u = float(r[:y])
            v = float(r[y + 1:])
            rad = u + v
        elif '-' in r:
            y = r.index('-')
            u = float(r[:y])
            v = float(r[y + 1:])
            rad = u - v
        elif '*' in r:
            y = r.index('*')
            u = float(r[:y])
            v = float(r[y + 1:])
            rad = u * v
        elif '/' in r:
            y = r.index('/')
            u = float(r[:y])
            v = float(r[y + 1:])
            rad = u / v
        else:
            rad = float(r)
    rad_to_deg()
else:
    print("Invalid input")


    

