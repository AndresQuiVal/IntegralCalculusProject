"""
Main entrance of app and UI logic
"""

import tkinter as tk
from general import *
import components as cp


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

# grid control container

main_entry = tk.Entry(main_area)
main_entry.pack(pady=20)

main_grid = tk.Frame(main_area, width=500, height=500, background=MAIN_WINDOW_COLOR)
main_grid.pack()

# 4 buttons for 4 options

tk.Button(main_grid, text="Left rectangle", width=15, height=2, command=lambda:solve_equation("left")).grid(row=0, column=0, pady=5, padx=5)
tk.Button(main_grid, text="Right rectangle", width=15, height=2, command=lambda:solve_equation("right")).grid(row=0, column=1, pady=5, padx=5)
tk.Button(main_grid, text="Midpoint rectangle", width=15, height=2, command=lambda:solve_equation("middle")).grid(row=1, column=0, pady=5, padx=5)
tk.Button(main_grid, text="Trapezoid", width=15, height=2, command=lambda:solve_equation("trapezoid")).grid(row=1, column=1, pady=5, padx=5)


def solve_equation(method : str):
    """
    Main function to solve the equation
    """
    pass

def main():
    window_esthetic()

if __name__ == "__main__":
    main()


root.mainloop()




