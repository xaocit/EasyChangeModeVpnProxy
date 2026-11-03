# Модуль с кастомным свитчом

from tkinter import *
from tkinter import ttk


class MyCustomSwitch(Canvas):

    def __init__(self, parent, width=48, height=22, comand=None):
        super().__init__(parent, width=width, height=height, bg=parent.cget("bg"), highlightthickness=0)

        self.width = width
        self.height = height
        self.comand = comand

        self._is_on = False

        self.slider_color_off = "#fafafa"
        self.slider_color_on = "#000000"

        self.bg_color_off = "#000000"
        self.bg_color_on = "#28C8F4"
 
        self.draw_switch()

        self.bind("<Button-1>", self.toggle)

    def draw_switch(self):

        bg_color = self.bg_color_off if not self._is_on else self.bg_color_on
        slider_color = self.slider_color_off if not self._is_on else self.slider_color_on

        self.create_arc(0, 0, self.height, self.height, start=-90, extent=-180, fill=bg_color, outline="", )
        self.create_arc(self.width-self.height, 0, self.width-1, self.height, start=-90, extent=180, fill=bg_color, outline="")


        x_left_of_rect = self.height // 2
        x_righ_of_rect = self.width - (self.height // 2)
        self.create_rectangle(x_left_of_rect - 1, 0, x_righ_of_rect + 1, self.height, fill=bg_color, outline="")

        # Всё для переключателя
        padding = 2
        c_x1 = padding
        c_y1 = padding
        c_x2 = self.height - padding
        c_y2 = self.height - padding

        self.create_oval(c_x1, c_y1, c_x2, c_y2, width=2, fill=slider_color, outline="")

    def toggle(self):
        pass

    def animate(self):
        pass

    def move_to_slider(self):
        pass

