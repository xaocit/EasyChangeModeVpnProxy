# Модуль с кастомным свитчом

import tkinter as tk


class MyCustomSwitch(tk.Canvas):

    def __init__(self, parent, mode: bool, width=48, height=22, variable=None, comand=None):
        super().__init__(parent, width=width, height=height, bg=parent.cget("bg"), highlightthickness=0)

        self.width = width
        self.height = height

        self._is_on = mode
        self.variable = variable
        self.comand = comand

        self.padding = 2
        self.x_right = self.width - self.height + self.padding
        self.x_left = self.padding
        self.current_x = 0 if (not self._is_on) else (self.x_right - self.padding)  # Определяем начальное положение кнопки в зависимости от состояния кнопки

        self.slider_color_off = "#fafafa"
        self.slider_color_on = "#000000"

        self.bg_color_off = "#000000"
        self.bg_color_on = "#28C8F4"

 
        self.draw_switch()

        self.bind("<Button-1>", self.toggle)


    def draw_switch(self):

        bg_color = self.bg_color_off if not self._is_on else self.bg_color_on
        slider_color = self.slider_color_off if not self._is_on else self.slider_color_on

        self.create_arc(0, 0, self.height, self.height, start=-90, extent=-180, fill=bg_color, outline="", tags="bg")
        self.create_arc(self.width-self.height, 0, self.width-1, self.height, start=-90, extent=180, fill=bg_color, outline="", tags="bg")


        x_left_of_rect = self.height // 2
        x_righ_of_rect = self.width - (self.height // 2)
        self.create_rectangle(x_left_of_rect - 1, 0, x_righ_of_rect + 1, self.height, fill=bg_color, outline="", tags="bg")

        # Всё для переключателя
        c_x1 = self.padding
        c_y1 = self.padding
        c_x2 = self.height - self.padding
        c_y2 = self.height - self.padding

        self.switch = self.create_oval(self.current_x + c_x1, c_y1, self.current_x + c_x2, c_y2, width=2, fill=slider_color, outline="", tags="slider")


    def toggle(self, event=None):

        self._is_on = not self._is_on

        if self.comand:
            self.comand(self._is_on)

        bg_color = self.bg_color_on if self._is_on else self.bg_color_off
        slider_color = self.slider_color_on if self._is_on else self.slider_color_off

        self.itemconfig("bg", fill=bg_color)
        self.itemconfig("slider", fill=slider_color)


        self.animate()


    def animate(self):
        """Логика анимации свитча"""

        target_x = self.x_left if not self._is_on else self.x_right # Определение цели движения
        step = 4 # Скорость движения

        # Движение вправо
        if self._is_on and (self.current_x < target_x):
            self.current_x = min(self.current_x + step, target_x)
            self.move_to_slider()
            self.after(10, self.animate)

        # Движение влево
        elif (not self._is_on) and (self.current_x > target_x):
            self.current_x = max(self.current_x - step, target_x)
            self.move_to_slider()
            self.after(10, self.animate)

    def move_to_slider(self):
        """Обновление координат свитча на холсте по значению self.current_x"""

        y1 = self.padding
        x2 = self.current_x + self.height - (self.padding * 2)
        y2 = self.height - self.padding

        self.coords("slider", self.current_x, y1, x2, y2)