# Модуль с собственными исключениями

class ProxyRegistryError(Exception):
    pass


class ParameterNotFoundError(ProxyRegistryError):
    """Класс ошибки реестра при неверном пути реестра"""

    def __init__(self, message: str = "Параметр не найден в реестре", details: str = None):

        self.message = message
        self.details = details

        super().__init__(self.message)


class ServerNotFoundError(ProxyRegistryError):
    """Класс ошибки реестра при отсутствии сервера"""

    def __init__(self, message: str = "Сервер не найден в реестре", details: str = None):

        self.message = message
        self.details = details

        super().__init__(self.message)


class AccessRightError(ProxyRegistryError):
    """Класс ошибки реестра при отсутствии прав доступа"""

    def __init__(self, message: str = "Нет необходимых прав доступа", details: str = None):

        self.message = message
        self.details = details

        super().__init__(self.message)


class OtherRegisterError(ProxyRegistryError):
    """Класс остальных ошибок реестра"""

    def __init__(self, message: str, details: str = None):

        self.message = f"Ошибка реестра: {message}"
        self.details = details

        super().__init__(self.message)