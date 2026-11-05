# Модуль с событиями по нажатиям кнопок

from typing import Callable

from tkinter import *

from services.interaction import set_proxy_settings

def switch_event(is_active: BooleanVar, label_on_or_off: Label, entry_ip: Entry):

    if is_active.get():
        label_on_or_off.config(text="Вкл.")
        entry_ip.config(state="normal", foreground="black")

    else:
        label_on_or_off.config(text="Откл.")
        entry_ip.config(state="readonly", foreground="gray")


def button_save_event(ip_port: str, enabled: bool, exit_app: Callable):
    set_proxy_settings(ip_port, enabled)
    exit_app()