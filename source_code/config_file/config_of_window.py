import sys
from pathlib import Path

# Имя окна
title_of_window = "Автопереключение режима подсоединения к wi-fi"

# Уникальный идентификатор приложения
app_id = "EasyChangeModeNetworkVpnProxy.product.1_0"

# Путь к иконке приложения в режиме редактирования и запуске .exe
if getattr(sys, 'frozen', False):
    path_of_icon = sys.executable
else:
    path_of_icon = Path(__file__).resolve().parent / "icon_app.ico"

# Задаем размер окна
window_size = (600, 400)

# Задаём возможность изменения размера окна по высоте и ширине
is_resizable = (False, False)