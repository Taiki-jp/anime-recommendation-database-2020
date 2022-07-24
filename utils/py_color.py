from dataclasses import dataclass
import time


@dataclass
class PyColor:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RETURN = "\033[07m"  # 反転
    ACCENT = "\033[01m"  # 強調
    FLASH = "\033[05m"  # 点滅
    RED_FLASH = "\033[05;41m"  # 赤背景+点滅
    BOLD = "\033[1m"  # 太字
    END = "\033[0m"
    GREEN_FLASH = "\33[05;32m"


if __name__ == "__main__":
    py_color = PyColor()
    print(py_color.FLASH + "flash" + py_color.END)
    print(py_color.BLUE, "blue", py_color.END)
    print(py_color.BLUE, py_color.FLASH, "blue and flash", py_color.END)
    print(py_color.BLUE, py_color.RETURN, "blue and return", py_color.END)
    print(py_color.RED_FLASH, "red_flash", py_color.END)
    print(py_color.CYAN, py_color.BOLD, "cyan and bold", py_color.END)
    print(py_color.GREEN_FLASH, "green flash", py_color.END)
