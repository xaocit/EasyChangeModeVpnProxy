# Главный модуль запуска приложения

from config_file.config_of_window import (title_of_window,
                                          path_of_icon,
                                          window_size, 
                                          is_resizable,
                                          )

from view.mainly_window import MainWindow
from presenter.control_elements import ProxyPresenter


def main():

    view = MainWindow(title_of_window=title_of_window,
                      path_of_icon=path_of_icon,
                      window_size=window_size,
                      is_resizable=is_resizable)

    presenter = ProxyPresenter(view=view)
    presenter.start()

if __name__ == "__main__":
    main()