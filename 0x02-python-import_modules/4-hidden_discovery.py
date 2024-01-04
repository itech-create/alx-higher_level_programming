#!/usr/bin/python3

import dis
import types

def print_names(obj):
    """Prints all names in obj."""
    print([name for name in dir(obj) if not name.startswith("__")])

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()

    module = types.ModuleType("hidden_4")
    exec(compile(code, "<string>", "exec"), module.__dict__)

    print_names(module)

