# Модуль для взаимодействия с настройками прокси через реестр

import winreg  # Доступ к настройкам
import ctypes  # Для применения изменений настроек реестра

def get_proxy_settings() -> tuple:

    registry_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path) as key:

            proxy_enable, _ = winreg.QueryValueEx(key, "ProxyEnable")

            try:
                proxy_server, _ = winreg.QueryValueEx(key, "ProxyServer")

            except FileNotFoundError:
                # Ошибка - не задан сервер
                pass

            # Преобразуем в привычный вид
            proxy_enable = bool(proxy_enable)
            proxy_server = str(proxy_server)[:str(proxy_server).find(':')]

            return (proxy_enable, proxy_server)
        
    except Exception as e:
        # Ошибка при обращении к реестру
        pass


def set_proxy_settings(ip_port: str, enabled: bool):

    registry_path = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_WRITE) as key:

            ip_port = ip_port + ":8080"
            mode = 1 if enabled else 0

            winreg.SetValueEx(key, "ProxyEnable", 0, winreg.REG_DWORD, mode)

            winreg.SetValueEx(key, "ProxyServer", 0, winreg.REG_SZ, ip_port)


        # Уведомляем систему об изменении настроек
        INTERNET_OPTION_REFRESH = 37
        INTERNET_OPTION_SETTINGS_CHANGED = 39

        wininet = ctypes.windll.wininet
        wininet.InternetSetOptionW(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
        wininet.InternetSetOptionW(0, INTERNET_OPTION_REFRESH, 0, 0)

    except Exception as e:
        pass # Не удалось изменить настройки