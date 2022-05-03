"""
Here goes all the math functions for solving integrals;
later on will be exported to main.py

NOTES:

base of rectangles:
base = (last_limit - first_limit) / number_rectangles

Height of rectangle:
f(x [left | right | middle]) 

Area of rectangle:
area_recangle = f(x [left | right | middle]) *  base

Area under curve:
integral = area_rectangle * number_rectangles

OUTPUT 'integral'
"""

def f(x : int, function : str):
    function.replace("x", str(x))
    return eval(function)


def get_left_rectangle(function, rectangles, first_limit, last_limit):
    if not function or not rectangles:
        return
    
    area_rectangles = 0
    base = (last_limit - first_limit) // rectangles

    if base <= 0:
        return -1 # invalid input, by now...

    for i in range(first_limit, last_limit, base):
        height = f(i, function)
        area_rectangles += base * height
    
    return area_rectangles
 

def get_right_rectangle(function, rectangles, first_limit, last_limit):
    if not function or not rectangles:
        return
    
    area_rectangles = 0
    base = (last_limit - first_limit) // rectangles
    
    if base <= 0:
        return -1 # invalid input, by now...

    for i in range(first_limit, last_limit, base):
        height = f(i + base, function)
        area_rectangles += base * height
    
    return area_rectangles

def get_middle_rectangle(function, rectangles, first_limit, last_limit):
    if not function or not rectangles:
        return
    
    area_rectangles = 0
    base = (last_limit - first_limit) // rectangles

    if base <= 0:
        return -1 # invalid input, by now...

    for i in range(first_limit + base, last_limit + 1, base):
        height = f((i + (i + base) / 2), function)
        area_rectangles += base * height
    
    return area_rectangles

def get_trapezoid_rectangle(function, rectangles, first_limit, last_limit):
    pass