# Файл с главным окном программы

from typing import Callable

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from view.custom_switch import MyCustomSwitch

from model.entry_validator import validate_max_symbols_input


class MainWindow:
    """Класс, реализующий методы по отрисовке элементов на окне и дающий контроль над ними через переменные"""

    def __init__(self, title_of_window: str, path_of_icon: str, window_size: tuple[int], is_resizable: tuple[bool]):
        """Создаём окно"""

        self._root = tk.Tk()  # создаем корневой объект - окно
        self._root.withdraw() # Скрываем окно, чтобы оно вывелось затем уже прогруженным

        self._root.title(title_of_window)  # устанавливаем заголовок окна
        self._root.iconbitmap(default=path_of_icon)


        # Задаем размер окна
        window_width, window_height = window_size

        # Получаем ширину и высоту экрана
        screen_width = self._root.winfo_screenwidth()
        screen_height = self._root.winfo_screenheight()

        # Вычисляем координаты X и Y для центрирования
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Устанавливаем размер и положение окна
        self._root.geometry(f'{window_width}x{window_height}+{x}+{y}')


        is_resizable_width, is_resizable_height = is_resizable  
        self._root.resizable(is_resizable_width, is_resizable_height)


    def get_input_data(self) -> tuple[tk.BooleanVar, str]:
        return (self._is_active_switch.get(), self._field_with_ip.get())


    def set_proxy_ui_state(self):
        """Меняет внешний вид элементов в зависимости от положения переключателя."""

        if self._is_active_switch.get():
            self._label_on_or_off_proxy_server.config(text="Вкл.")
            self._field_with_ip.config(state="normal", foreground="black")

        else:
            self._label_on_or_off_proxy_server.config(text="Откл.")
            self._field_with_ip.config(state="readonly", foreground="gray")


    def set_initial_values(self, start_mode_switch: bool, start_ip: str):

        self._start_mode_of_button = start_mode_switch
        self._start_ip_port = start_ip


    def _draw_elements(self):

        ###### Надпись: Использовать прокси-сервер:
        label_using_proxy_server = ttk.Label(text="Использовать прокси-сервер: ", 
                        font=("Times New Roman", 14))

        label_using_proxy_server.grid(row=0, column=0, pady=10 ,sticky="we")


        ###### Свитч
        self._is_active_switch = tk.BooleanVar(value=self._start_mode_of_button)
    
        ctk_switch = MyCustomSwitch(self._root, 
                                    mode=self._start_mode_of_button,
                                    comand=lambda state: [
                                        self._is_active_switch.set(state),
                                        self.set_proxy_ui_state()
                                        ]
                                    )

        ctk_switch.grid(row=0, column=1, pady=10, sticky="we")


        ###### Надпись: Вкл. ИЛИ Откл.
        start_text = "Вкл." if self._start_mode_of_button else "Откл."
        self._label_on_or_off_proxy_server = ttk.Label(text=start_text, 
                        font=("Times New Roman", 14))

        self._label_on_or_off_proxy_server.grid(row=0, column=2, pady=10, sticky="we")


        ###### Надпись: IP-адрес прокси-сервера:
        label_using_proxy_server = ttk.Label(text="IP-адрес прокси-сервера: ", 
                        font=("Times New Roman", 14))

        label_using_proxy_server.grid(row=2, column=0, pady=10, sticky="we")


        ###### Поле для ввода IP
        self._field_with_ip = ttk.Entry(width=20, 
                                        font=("Times New Roman", 16))
        self._field_with_ip.insert(0, self._start_ip_port)

        start_state = "normal" if self._start_mode_of_button else "readonly"
        start_fg = "black" if self._start_mode_of_button else "gray"

        validate_count_of_symbols = (self._root.register(validate_max_symbols_input), '%P')
        self._field_with_ip.config(state=start_state, foreground=start_fg, validatecommand=validate_count_of_symbols, validate='key')

        self._field_with_ip.grid(row=3, column=0, pady=10, sticky="we")


        ###### Кнопка: Сохранить и выйти
        btn_save_all = ttk.Button(text="Сохранить и выйти", 
                                  command=self._on_save)

        btn_save_all.grid(row = 4, column=0, pady=10, sticky="we")


    def bind_events(self, on_save: Callable):
        self._on_save = on_save


    def run(self):

        ###### Рисуем элементы
        self._draw_elements()

        self._root.deiconify()

        self._root.mainloop()


    def showerror(self, e: str):
        messagebox.showerror(message=e)


    def close(self):
        self._root.destroy()