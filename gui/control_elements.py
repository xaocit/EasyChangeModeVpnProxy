# Модуль с событиями по нажатиям кнопок

from tkinter import *

def checkbutton_event(is_active: BooleanVar, label_on_or_off: Label, entry_ip: Entry):

    if is_active.get():
        label_on_or_off.config(text="Вкл.")
        entry_ip.config(state="normal", foreground="black")

    else:
        label_on_or_off.config(text="Откл.")
        entry_ip.config(state="readonly", foreground="gray")