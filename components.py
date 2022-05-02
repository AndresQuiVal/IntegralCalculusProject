import tkinter as tk
from general import FONT_ATTRS

class AppLabelTitle(tk.Label):
    def __init__(self, master, *args, **kwargs): 
        tk.Label.__init__(self, master, *args, **kwargs)  
        self.configure(font = tuple(FONT_ATTRS[0:2]), fg=FONT_ATTRS[2])


class AppLabel(tk.Label):
    def __init__(self, master, *args, **kwargs): 
        tk.Label.__init__(self, master, *args, **kwargs) 
        FONT_ATTRS[1] = 10
        FONT_ATTRS[2] = '#707070'
        self.configure(font = tuple(FONT_ATTRS[0:2]), fg=FONT_ATTRS[2])


class AppButton(tk.Canvas):
    def __init__(self, parent, width, height, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1, 
            relief="raised", highlightthickness=0)
        self.command = command

        padding = 4
        id = self.create_oval((padding,padding,
            width+padding, height+padding), outline="white", fill="white")
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()