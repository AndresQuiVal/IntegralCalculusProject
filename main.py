"""
Main entrance of app and UI logic
"""

from dataclasses import dataclass
import components as cp
from app_logic import *
from general import *
import tkinter as tk



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
rectangles_number = tk.StringVar()

# grid control container

main_entry = tk.Entry(main_area, textvariable=function)
main_entry.insert(0, 'function expression')
main_entry.pack(pady=20)


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


def get_integral(method : str):
    """
    Main function to solve the equation
    """
    global rectangles_number, function

    rectangles_number_int = int(rectangles_number.get())
    function_str = function.get()
    
    if method == "left":
        res = get_left_rectangle(function_str, rectangles_number_int, 1, 500)
    elif method == "right":
        res = get_right_rectangle(function_str, rectangles_number_int, 1, 500)
    elif method == "middle":
        res = get_middle_rectangle(function_str, rectangles_number_int, 1, 500)
    elif method == "trapezoid":
        res = get_trapezoid_rectangle(function_str, rectangles_number_int, 1, 500)

    print(res)

    # render data...

def main():
    window_esthetic()

if __name__ == "__main__":
    main()


root.mainloop()




