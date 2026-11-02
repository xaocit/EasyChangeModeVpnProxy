# Модуль с событиями по нажатиям кнопок

from tkinter import *
from customtkinter import CTkSwitch

def checkbutton_event(ctk_switch: CTkSwitch, is_active: BooleanVar, label_on_or_off: Label, entry_ip: Entry):

    if is_active.get():
        ctk_switch.config()
        label_on_or_off.config(text="Вкл.")
        entry_ip.config(state="normal", foreground="black")

    else:
        label_on_or_off.config(text="Откл.")
        entry_ip.config(state="readonly", foreground="gray")