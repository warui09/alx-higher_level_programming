#!/usr/bin/python3

if __name__ == "__main__":
    import importlib

    hidden_4 = importlib.import_module("hidden_4")

    attribute_names = dir(hidden_4)

    for name in sorted(attribute_names):
        if not name.startswith("__"):
            print(name)
