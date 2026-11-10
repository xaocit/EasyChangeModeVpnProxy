# Модуль с валидациями вводимого ip

import re

def validate_input(ip: str) -> bool:

    result = validate_max_symbols_input(ip) and validate_string_in_input(ip)

    if result:
        return True
    
    return False

def validate_max_symbols_input(ip: str) -> bool:
    return len(ip) < 16

def validate_string_in_input(ip: str) -> bool:

    # Строгий вариант без ведущих нулей (кроме самого нуля)
    strict_octet = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    strict_pattern = re.compile(rf'\b{strict_octet}(?:\.{strict_octet}){{3}}\b')

    return bool(strict_pattern.fullmatch(ip))