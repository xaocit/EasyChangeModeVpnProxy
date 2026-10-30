# Файл с главным окном программы

from tkinter import *
from tkinter import ttk

from validators.entry_validator import validate_max_symbols_input

def create_window(title_of_window: str, path_of_icon: str, window_size: tuple[int], is_resizable: tuple[bool]):
    """Функция создания окна"""
 
    root = Tk()  # создаем корневой объект - окно

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
    build_window()

    root.mainloop()


def build_window():
    """Функция, где собираем всё, что будем отображать на экране"""

    show_label_using_proxy_server()
    show_radiobutton_on_or_off()
    show_label_on_or_off()

    show_label_ip_adress_proxy_server()
    show_entry_ip()



def show_label_using_proxy_server():


    label_using_proxy_server = ttk.Label(text="Использовать прокси-сервер: ", 
                      font=("Times New Roman", 14))

    label_using_proxy_server.grid(row=0, column=0, pady=10 ,sticky="we")


def show_radiobutton_on_or_off():


    radiobutton_vpn_proxy = ttk.Radiobutton()

    radiobutton_vpn_proxy.grid(row=0, column=1, pady=10, sticky="we")


def show_label_on_or_off():


    label_on_or_off_proxy_server = ttk.Label(text="Откл.", 
                    font=("Times New Roman", 14))

    label_on_or_off_proxy_server.grid(row=0, column=2, pady=10, sticky="we")



def show_label_ip_adress_proxy_server():


    label_using_proxy_server = ttk.Label(text="IP-адрес прокси-сервера: ", 
                      font=("Times New Roman", 14))

    label_using_proxy_server.grid(row=2, column=0, pady=10, sticky="we")


def show_entry_ip():


    entry_field_with_ip = ttk.Entry(width=20, 
                                    font=("Times New Roman", 16))

    validator = (entry_field_with_ip.register(validate_max_symbols_input), '%P')
    entry_field_with_ip.config(validate='key', validatecommand=validator)
    
    entry_field_with_ip.grid(row=3, column=0, pady=10, sticky="we")