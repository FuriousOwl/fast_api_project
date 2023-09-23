from enum import Enum


class Messages(str, Enum):
    BUILDING_INSTALLATION_NOT_ALLOWED: str = \
        "Установка здания в данном месте невозможна, так как оно пересекается с другими объектами."
    BUILDING_INSTALLATION_ALLOWED: str = "Установка здания в данном месте возможна."
    SERVER_ERROR: str = "Произошла ошибка сервера"
