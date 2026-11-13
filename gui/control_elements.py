# Модуль с событиями по нажатиям кнопок

from typing import Callable

import tkinter as tk
from tkinter import messagebox

from validators.entry_validator import validate_string_in_input

from services.interaction import set_proxy_settings

def switch_event(is_active: tk.BooleanVar, label_on_or_off: tk.Label, entry_ip: tk.Entry):

    if is_active.get():
        label_on_or_off.config(text="Вкл.")
        entry_ip.config(state="normal", foreground="black")

    else:
        label_on_or_off.config(text="Откл.")
        entry_ip.config(state="readonly", foreground="gray")


def button_save_event(ip_port: str, enabled: bool, exit_app: Callable):

    if validate_string_in_input(ip_port):
        set_proxy_settings(ip_port, enabled)
        exit_app()

    else:
        messagebox.showwarning(message="Ошибка ввода! Введите корректный ip-адрес !!!")
        return