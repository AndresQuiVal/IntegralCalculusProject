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

def f(x : float, function : str):
    function = function.replace("x", str(x))
    try:
        return eval(function)
    except ZeroDivisionError:
        return 0 # if its 0, area is not counted
    


def get_left_rectangle(function, rectangles, first_limit, last_limit):
    if not function or not rectangles:
        return
    
    area_rectangles = 0
    base = (last_limit - first_limit) / rectangles

    if base < 0:
        return -1 # invalid base
    
    i = first_limit

    while i < last_limit:
        height = f(i, function)
        area_rectangles += base * height
        i += base
    
    return area_rectangles
 

def get_right_rectangle(function, rectangles, first_limit, last_limit):
    if not function or not rectangles:
        return
    
    area_rectangles = 0
    base = (last_limit - first_limit) / rectangles
    
    if base < 0:
        return -1 # invalid input, by now...
    
    i = first_limit
    while i < last_limit:
        height = f(i + base, function)
        area_rectangles += base * height
        i += base
    
    return area_rectangles

def get_middle_rectangle(function, rectangles, first_limit, last_limit):
    if not function or not rectangles:
        return
    
    area_rectangles = 0
    base = (last_limit - first_limit) / rectangles

    if base < 0:
        return -1 # invalid input, by now...

    i = first_limit
    while i < last_limit:
        height = f((i + (i + base) / 2), function)
        area_rectangles += base * height
        i += base
    
    return area_rectangles

def get_trapezoid_rectangle(function, rectangles, first_limit, last_limit):
    pass