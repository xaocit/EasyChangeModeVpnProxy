# Главный модуль запуска приложения

from config_file.config_of_window import (title_of_window,
                                          path_of_icon,
                                          window_size, 
                                          is_resizable,
                                          )

from gui.mainly_window import create_window

def main():
    create_window(title_of_window, path_of_icon, window_size, is_resizable)

if __name__ == "__main__":
    main()