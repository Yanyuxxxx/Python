import math

def area(radius):
    return math.pi * radius **2

def absolute_value(x):
    if x < 0:
        return -x
    if x >= 0:
        return x


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    resurt = math.sqrt(dsquared)
    return resurt


x = distance(1, 2, 4, 6)

print(x)

