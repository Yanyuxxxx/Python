
import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n, sn):
    angle = 360.0/n
    for i in range(sn):
        t.fd(length)
        t.lt(angle)

def circle(t, r, angle):


    c = 2 * math.pi * r
    n = 40
    length = c / n
    sn = 40 * angle / 360

    polygon(t, length, n, sn)



bob = turtle.Turtle()

if 0 :
    print('1')
else:
    print('0')


# square(bob, 200)
# polygon(bob, 100, 10)
circle(bob, 100, 180)


while(1):
   pass



