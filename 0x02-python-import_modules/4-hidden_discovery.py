#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Load the compiled module
    module_name = "hidden_4"
    module_path = "./hidden_4.pyc"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter and print names that do not start with __
    filtered_names = [name for name in names if not name.startswith("__")]
    for name in sorted(filtered_names):
        print(name)
