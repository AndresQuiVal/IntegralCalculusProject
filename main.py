"""
Main entrance of app and UI logic
"""

import matplotlib.pyplot as plt
import components as cp
from app_logic import *
from general import *
import tkinter as tk
import numpy as np




root = tk.Tk()

# define esthetic of window
def window_esthetic():
    global root
    root.configure(bg=MAIN_WINDOW_COLOR)

# defining layouts ---

# header
headbar = tk.Frame(root, background=MAIN_WINDOW_COLOR, height=40, borderwidth=2)
headbar.pack(expand=False, fill='both', side='top', anchor='nw')

# main content area
main_area = tk.Frame(root, background=MAIN_WINDOW_COLOR, width=500, height=500)
main_area.pack(expand=True, fill='both', side='right', padx=10, pady=10)

# defining widgets -----

title = cp.AppLabelTitle(headbar, text="Tablify", background=MAIN_WINDOW_COLOR, font=('Arial', 15))
title.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title = cp.AppLabel(main_area, text="By: \nJJ & Andrés Quiroz", background=MAIN_WINDOW_COLOR)
title.pack(pady=20)


# String vars

function = tk.StringVar()
left_limit = tk.StringVar()
right_limit = tk.StringVar()
rectangles_number = tk.StringVar()

# grid control container
tk.Button(main_area, text="Dont now how to enter function?", width=25, height=1, command=lambda:tutorial_function_enter()).pack()

main_entry = tk.Entry(main_area, textvariable=function)
main_entry.insert(0, 'function expression')
main_entry.pack(pady=20)

limits_container = tk.Frame(main_area, background=MAIN_WINDOW_COLOR)
limits_container.pack(pady=5)

main_entry = tk.Entry(limits_container, textvariable=left_limit)
main_entry.insert(0, 'Left limit')
main_entry.grid(row=0, column=0, padx=3)

main_entry = tk.Entry(limits_container, textvariable=right_limit)
main_entry.insert(0, 'Right limit')
main_entry.grid(row=0, column=1, padx=3)


rectangles_title = cp.AppLabel(main_area, text="Number of rectangles:", background=MAIN_WINDOW_COLOR)
rectangles_title.pack()

rectangles = tk.Scale(main_area, orient=tk.HORIZONTAL, variable=rectangles_number, from_=0, to=1000, background=MAIN_WINDOW_COLOR, bd=0)
rectangles.pack(pady=20)


main_grid = tk.Frame(main_area, width=500, height=500, background=MAIN_WINDOW_COLOR)
main_grid.pack()

# 4 buttons for 4 options

tk.Button(main_grid, text="Left rectangle", width=15, height=2, command=lambda:get_integral("left")).grid(row=0, column=0, pady=5, padx=5)
tk.Button(main_grid, text="Right rectangle", width=15, height=2, command=lambda:get_integral("right")).grid(row=0, column=1, pady=5, padx=5)
tk.Button(main_grid, text="Midpoint rectangle", width=15, height=2, command=lambda:get_integral("middle")).grid(row=1, column=0, pady=5, padx=5)
tk.Button(main_grid, text="Trapezoid", width=15, height=2, command=lambda:get_integral("trapezoid")).grid(row=1, column=1, pady=5, padx=5)

# result frame

res_frame = tk.Frame(main_area, background=MAIN_WINDOW_COLOR)
res_frame.pack(padx=10, pady=10)
    


def tutorial_function_enter():
    """
    Opens a new window explaining how to enter correctly a function
    """
    description = """
        Entering your function is the first step to use the program, 
        first let's define the operands of the app:

        + : Defines a binary sum between operands
        - : Defines a binary substraction between operands
        * : Defines a binary multiplication between operands
        / : Defines a binary division between operands
        ** : Defines a binary pow between operands in form a ** b (example = x**2)
        
        Examples of how to enter your function:

        -> 2 ** x (same as 2^x)
        -> x**2 + 2*x + 4  (same as x^2 + 2x + 4)
        -> 2 (same as 2)
        -> -x**4 - 2*x (same as -x^2 - 2x)
        -> etc

        NOTE:

        Logarithm, Trigonometric and Exponentials are not currently
        available in this version, soon will be implemented! ;)
    """
    
    tutorial_window = tk.Toplevel(root, background=MAIN_WINDOW_COLOR)

    cp.AppLabelTitle(tutorial_window, text="Tablify - How to enter function for Dummies", background=MAIN_WINDOW_COLOR, font=('Arial', 15)).pack()
    cp.AppLabel(tutorial_window, text=description, background=MAIN_WINDOW_COLOR).pack(pady=10)

    tk.Button(tutorial_window, text="Im ready to use the app!", command=tutorial_window.destroy).pack(pady=10)

def get_integral(method : str):
    """
    Main function to solve the equation
    """

    global rectangles_number, function

    def clear_res_content():
        global res_frame
        for widgets in res_frame.winfo_children():
            widgets.destroy()
    
    def show_graph(f, method, rectangles, left, right):
        f = lambda x : eval(function_str)
        a = left; b = right; N = rectangles
        n = rectangles

        x = np.linspace(a,b,N+1)
        y = f(x)

        X = np.linspace(a,b,n*N+1)
        Y = f(X)

        plt.figure(figsize=(7,3))

        if method == "left":
            plt.subplot(1,3,1)
            plt.plot(X,Y,'b')
            x_left = x[:-1] # Left endpoints
            y_left = y[:-1]
            plt.plot(x_left,y_left,'b.',markersize=10)
            plt.bar(x_left,y_left,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
            plt.title('Left Riemann Sum, N = {}'.format(N))

        elif method == "middle":
            plt.subplot(1,3,1)
            plt.plot(X,Y,'b')
            x_mid = (x[:-1] + x[1:])/2 # Midpoints
            y_mid = f(x_mid)
            plt.plot(x_mid,y_mid,'b.',markersize=10)
            plt.bar(x_mid,y_mid,width=(b-a)/N,alpha=0.2,edgecolor='b')
            plt.title('Midpoint Riemann Sum, N = {}'.format(N))
        
        elif method == "right":
            plt.subplot(1,3,1)
            plt.plot(X,Y,'b')
            x_right = x[1:] # Left endpoints
            y_right = y[1:]
            plt.plot(x_right,y_right,'b.',markersize=10)
            plt.bar(x_right,y_right,width=-(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
            plt.title('Right Riemann Sum, N = {}'.format(N))
        
        elif method == "trapezoid": 
            # TODO: AQUI VA EL CODIGO DE CONSTRUCCION DE LA GRAFICA DEL TRAPEZOIDE
            # USANDO LAS SUMAS DE LOS MISMOS...
            pass

        plt.show()

    
    
    rectangles_number_int = int(rectangles_number.get())
    function_str = function.get()
    
    if not "x" in function_str: # means is a constant function...
        function_str += "+0*x"
    
    if method == "left":
        res = get_left_rectangle(function_str, rectangles_number_int, int(left_limit.get()), int(right_limit.get()))
    elif method == "right":
        res = get_right_rectangle(function_str, rectangles_number_int, int(left_limit.get()), int(right_limit.get()))
    elif method == "middle":
        res = get_middle_rectangle(function_str, rectangles_number_int, int(left_limit.get()), int(right_limit.get()))
    elif method == "trapezoid":
        res = get_trapezoid_rectangle(function_str, rectangles_number_int, int(left_limit.get()), int(right_limit.get()))

    print(res)
    clear_res_content()

    # result label
    res_label = cp.AppLabel(res_frame, text=f"Aproximate Area result: {res} cm^2", background=MAIN_WINDOW_COLOR)
    res_label.pack()

    # render graph
    show_graph(function_str, method, int(rectangles_number.get()), int(left_limit.get()), int(right_limit.get()))


def main():
    window_esthetic()

if __name__ == "__main__":
    main()


root.mainloop()




