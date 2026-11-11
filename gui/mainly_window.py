# Файл с главным окном программы

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

from .custom_switch import MyCustomSwitch
from .control_elements import (switch_event,
                               button_save_event)

from validators.entry_validator import validate_max_symbols_input

from services.interaction import (get_proxy_settings)

from my_exceptions.custom_exceptions import ProxyRegistryError


def create_window(title_of_window: str, path_of_icon: str, window_size: tuple[int], is_resizable: tuple[bool]):
    """Функция создания окна"""
 
    root = Tk()  # создаем корневой объект - окно
    root.withdraw() # Скрываем окно, чтобы оно вывелось затем уже прогруженным

    try:
        root.title(title_of_window)  # устанавливаем заголовок окна
        root.iconbitmap(default=path_of_icon)


        # Задаем размер окна
        window_width, window_height = window_size

        # Получаем ширину и высоту экрана
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Вычисляем координаты X и Y для центрирования
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Устанавливаем размер и положение окна
        root.geometry(f'{window_width}x{window_height}+{x}+{y}')


        is_resizable_width, is_resizable_height = is_resizable
        root.resizable(is_resizable_width, is_resizable_height)


        ## Действия по размещению элементов на странице
        draw_elements = DrawElements(root)

        # Показываем окно, если всё прошло успешно
        root.deiconify()

        root.mainloop()

    except ProxyRegistryError as e:
        messagebox.showerror(title="Критическая ошибка", message=str(e))
        root.destroy()


class DrawElements:
    """Класс, реализующий методы по отрисовке элементов на окне и дающий контроль над ними через переменные"""

    def __init__(self, root: Tk):

        self._root = root

        # Стартовое положение кнопки и значение ip
        self._start_mode_of_button, self._start_ip_port = get_proxy_settings()

        label_using_proxy_server = self._show_label_using_proxy_server()
        self._is_active_ctk_switch, self._checkbutton_on_or_off = self._show_checkbutton_on_or_off()
        self._label_on_or_off = self._show_label_on_or_off()

        label_ip_adress_proxy_server = self._show_label_ip_adress_proxy_server()
        self._entry_ip = self._show_entry_ip()

        self._btn_save_all = self._show_button_save_all()


    def get_checkbutton(self):
        return (self._is_active_checkbutton, self._checkbutton_on_or_off)

    def get_entry_ip(self):
        return self._entry_ip

    def get_btn_save_all(self):
        return self._btn_save_all

    def get_label_on_or_off(self):
        return self._label_on_or_off


    def _show_label_using_proxy_server(self) -> ttk.Label:


        label_using_proxy_server = ttk.Label(text="Использовать прокси-сервер: ", 
                        font=("Times New Roman", 14))

        label_using_proxy_server.grid(row=0, column=0, pady=10 ,sticky="we")

        return label_using_proxy_server


    def _show_checkbutton_on_or_off(self) -> tuple[BooleanVar, ctk.CTkSwitch]:

        is_active = BooleanVar()

        ctk_switch = MyCustomSwitch(self._root, 
                                    mode=self._start_mode_of_button,
                                    comand=lambda state: [
                                        is_active.set(state),
                                        switch_event(is_active, self.get_label_on_or_off(), self.get_entry_ip())
                                        ]
                                    )

        ctk_switch.grid(row=0, column=1, pady=10, sticky="we")


        return (is_active, ctk_switch)


    def _show_label_on_or_off(self) -> ttk.Label:


        start_text = "Вкл." if self._start_mode_of_button else "Откл"
        label_on_or_off_proxy_server = ttk.Label(text=start_text, 
                        font=("Times New Roman", 14))

        label_on_or_off_proxy_server.grid(row=0, column=2, pady=10, sticky="we")

        return label_on_or_off_proxy_server


    def _show_label_ip_adress_proxy_server(self) -> ttk.Label:


        label_using_proxy_server = ttk.Label(text="IP-адрес прокси-сервера: ", 
                        font=("Times New Roman", 14))

        label_using_proxy_server.grid(row=2, column=0, pady=10, sticky="we")

        return label_using_proxy_server


    def _show_entry_ip(self) -> ttk.Entry:


        entry_field_with_ip = ttk.Entry(width=20, 
                                        font=("Times New Roman", 16))
        entry_field_with_ip.insert(0, self._start_ip_port)

        start_state = "normal" if self._start_mode_of_button else "readonly"
        start_fg = "black" if self._start_mode_of_button else "gray"

        validate_count_of_symbols = (self._root.register(validate_max_symbols_input), '%P')
        entry_field_with_ip.config(state=start_state, foreground=start_fg, validatecommand=validate_count_of_symbols, validate='key')

        entry_field_with_ip.grid(row=3, column=0, pady=10, sticky="we")

        return entry_field_with_ip


    def _show_button_save_all(self) -> ttk.Button:


        btn_save_all = ttk.Button(text="Сохранить и выйти", 
                                  command=lambda: button_save_event(self._entry_ip.get(), self._is_active_ctk_switch.get(), self._root.destroy))


        btn_save_all.grid(row = 4, column=0, pady=10, sticky="we")

        return btn_save_all


class DestroyApp:

    def __init__(self, root: Tk):
        root.destroy()