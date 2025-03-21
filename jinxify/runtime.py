import builtins
import sys
from typing import Any
import colorama

class PrintWrapper:
    def __init__(self):
        colorama.init()
        self.has_color = True  # force color output


class PrintWrapper:
    """JavaScript-style console replacement with colors"""
    
    def __init__(self):
        # checking "can its run colors?""
        self.has_color = sys.stdout.isatty()

    def _colorize(self, text: str, code: int) -> str:
        """Wrap text in ANSI color codes if supported"""
        return f"\033[{code}m{text}\033[0m" if self.has_color else text

    def log(self, *args: Any, **kwargs: Any) -> None:
        """Standard logging"""
        builtins.print(*args, **kwargs)
    
    def warn(self, *args: Any, **kwargs: Any) -> None:
        """Yellow warning message"""
        warning_text = self._colorize("WARNING:", 93)  # yellow
        builtins.print(f"{warning_text}", *args, **kwargs)

    def error(self, *args: Any, **kwargs: Any) -> None:
        """Red error message"""
        error_text = self._colorize("ERROR:", 91)  # redd
        builtins.print(f"{error_text}", *args, **kwargs)

print = PrintWrapper()