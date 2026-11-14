# Модуль с событиями по нажатиям кнопок

from typing import Callable

from model.custom_exceptions import ProxyRegistryError
from model.entry_validator import validate_string_in_input
from model.interaction import (get_proxy_settings,
                                set_proxy_settings)

from view.mainly_window import MainWindow


class ProxyPresenter:

    def __init__(self, view: MainWindow):

        self._view = view


    def start(self):

        try:
            self.set_initial_start_values()
            self._view.bind_events(self._handle_save)
            self._view.run()

        except ProxyRegistryError as e:
            self._view.showerror(f"Ошибка реестра при попытке сохранить настройки: {e}")
            self._view.close()


    def set_initial_start_values(self):

        is_enabled, ip = get_proxy_settings()
        
        self._view.set_initial_values(is_enabled, ip)


    def _handle_save(self):

        is_enabled, ip = self._view.get_input_data()

        if not validate_string_in_input(ip):
            self._view.showerror("Ошибка! Введите корректный ip-адрес !!!")
            return

        try:
            set_proxy_settings(is_enabled, ip)
            self._view.close()

        except ProxyRegistryError as e:
            self._view.showerror(f"Ошибка реестра при попытке сохранить настройки: {e}")
            self._view.close()
