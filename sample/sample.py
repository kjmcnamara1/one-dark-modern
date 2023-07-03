import re
from pathlib import Path

MODULE_CONST = re.compile(r"^module\.(\w+)$")

list_comprehension = [i for i in range(10)]


class MyClass:
    class_var: dict[str, bool] = {"key": True, "baz": False}

    def __init__(self) -> None:
        self.foo = "bar"
        self.num = 5
        self.home=Path('~')
        return

    @staticmethod
    def my_static_method(x:int, y:float=5.0, *args) -> float:
        """docstring"""
        print("This is a static method.")
        return (x * y) - (x + y)


# Calling the static method without creating an instance of the class
MyClass.my_static_method(2, extra=3+4j)
